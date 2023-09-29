import wikipedia
from bs4 import BeautifulSoup
# import requests
# import re
import json
import os
import argparse
import sys

parser = argparse.ArgumentParser(description="Wikislide parser")
parser.add_argument("--title", dest="title", type=str, default="Toulouse", help="Name of the article")
parser.add_argument("--language", dest="language", default="en", type=str, help="Language of the article")

parser.add_argument("--related", dest="related", action='store_true', help="Find all wikipedia related too")
parser.add_argument("--limit", dest="limit", default="50", type=int, help="Max nb of articles")
args = parser.parse_args()

def parse_wiki(title="Toulouse", lang="en"):
    try:
        # print("parsing {} wikipedia article".format(title))
        
        # Set the language of the Wikipedia page
        wikipedia.set_lang(args.language)
        # Set the title of the Wikipedia page
        # 
        # Make output dirs
        os.makedirs("Wikipedia", exist_ok=True)
        os.makedirs("Wikipedia/" + title, exist_ok=True)
        # img_dir = "output/" + title + "/images"
        # os.makedirs(img_dir, exist_ok=True)

        # Fetch the content of the Wikipedia page
        page = wikipedia.page(title, auto_suggest=False)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(page.html(), "html.parser")
        # Get the title of the article
        article_title = page.title

        # Create a list to store the hierarchy of the article
        hierarchy = []

        # Add the title of the article to the hierarchy list
        hierarchy.append(article_title)

        # Find all section headings in the article
        # categories = soup.find("div", class_="reflist")
        # ref = []
        # ref = categories.text.split("^")

        # print(ref)

        headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
        mi = soup.findAll(["mi", "mo", "mrow"])
        for c in mi:
            # print(c)
            c.decompose()

        punctuation = {'.', ',', ':', ';', '!', '?'}
        # Loop through each section heading and add its title, content, and images to the hierarchy list
        for heading in headings:
            # Get the title of the section
            section_title = heading.text
            section_title = section_title.replace("[edit]", "")
            images_with_captions = []
            captions = []
            # Get the content of the section
            section_content = []
            
            tables = []
            big_figures = []
            count_big_fig = 0
            for sibling in heading.find_next_siblings():
                
                # count for big figures
               
                if sibling.name.startswith("h"):
                    break
                if sibling.name == "p":
                    # mi = sibling.findAll(["mi", "mo", "mrow"])
                    # for c in mi:
                    #     # print(c)
                    #     c.decompose()
                    section_text = ""
                    for a in sibling.contents:
                        if a.text.strip() != "" and a.name in {"span", "a","i", "b", None}:
                            if a.name == "span" and a.get("class") is not None:
                                if a.get("class")[0] == "mwe-math-element":
                                    section_content.append({"tag": "math-inline", "content": a.text.strip()})
                                elif a.get("class")[0] == "texhtml":
                                    section_content.append({"tag": "texhtml", "content": a.text.strip()})
                            else:
                                section_content.append({"tag": a.name, "content": a.text})
                            # else:
                            #     if a.text.strip()[0] in punctuation:
                            #         section_text += a.text.strip()
                            #     else:
                                    # section_text += " " + a.text.strip()
                        ## big figure in a paragraph
                        if a.name == "div":
                            if a.get("class")[0] == "mwe-math-element":
                                fig = a.findAll("img")
                                for f in fig:
                                    print("YO")
                                    print(f)
                                    # print(f.get("alt").strip())
                                    big_figures.append(f.get("alt").strip())
                                    section_content.append({"tag":"big_fig_ref", "content":count_big_fig})
                                    count_big_fig += 1
                    # section_text = re.sub("\[[0-9]*\]", '', section_text) 
                    # section_content.append(section_text.strip())
                    section_content.append({"tag": "end", "content": "\n"})
                    
                if sibling.name == "figure":
                    ## image
                    a_img = sibling.findAll("a")
                    for a in a_img:
                        image_url = ""
                        caption = ""
                        for img in a.findAll("img"):
                            # image_url = img.get("srcset")
                            # image_url = image_url.split(" ")[-2]
                            image_url = img.get("src")
                            if image_url.startswith("//"):
                                image_url = "https:" + image_url
                            # print(image_url)
                            # response = requests.get(image_url)
                            # image_file = open(img_dir + "/" + image_url.split('/')[-1].split('.')[0].replace("%", "") + ".jpg", "wb")
                            # image_file.write(response.content)
                            # image_file.close()
                            # images.append(img_dir + "/" + image_url.split('/')[-1].split('.')[0].replace("%", "") + ".jpg")
                            
                            # images.append(image_url)
                        # Find captions associated to the images
                        for div in a.find_next_siblings("figcaption"):
                                            #     c.decompose()
                            caption_content = []
                            for b in div.contents:
                                if b.text.strip() != "" and b.name in {"span", "a", None}:
                                    if b.name == "span" and b.get("class") is not None:
                                        if b.get("class")[0] == "mwe-math-element":
                                            caption_content.append({"tag": "math-inline", "content": b.text.strip()})
                                        elif b.get("class")[0] == "texhtml":
                                            caption_content.append({"tag": "texhtml", "content": b.text.strip()})
                                    else:
                                        caption_content.append({"tag": b.name, "content": b.text})
                            # caption = div.text
                            # for cap in div.findAll():
                            #     caption += cap.text
                            images_with_captions.append({"caption": caption_content, "image": image_url})

                    ## code

                    if sibling.get("class") is not None and sibling.get("class")[0] == "mw-highlight":
                        programming_lang = sibling.get("class")[1].split("-")[-1]
                        section_content.append({"tag": "code", "lang":programming_lang, "content":sibling.text.strip()})
                    # get table
                    for tb in sibling.findAll("table"):
                        tables.append(tb.prettify())
                # get list
                
                if sibling.name in {"ul", "ol"}:
                    ul = {"tag": sibling.name, "content":[]}
                    
                    mi = sibling.findAll(["mrow"])
                    for c in mi:
                        # print(c)
                        c.decompose()
                    for a in sibling.contents:
                        li = []
                        if a.name == "li":
                            b = a.contents
                            for c in b:
                                if c.name != "span":
                                    li.append({"tag": c.name, "content": c.text})
                                if c.name == "span":
                                    if c.get("class") is not None and c.get("class")[0] == "texhtml":
                                        li.append({"tag": "texhtml", "content": str(c)})
                            ul["content"].append(li)
                    section_content.append(ul)
                    ## images in gallery
                    ul_gallery = sibling.findAll("img", {"class": "mw-file-element"})
                    for img in ul_gallery:
                            caption_content = []
                            image_url = img.get("src")
                            if image_url.startswith("//"):
                                image_url = "https:" + image_url
                            images_with_captions.append({"caption": caption_content, "image": image_url})
                            

                    
                ## get table
                
                if sibling.name == "table":
                    tables.append(sibling.prettify())
                ## get big figures
                if sibling.name == "dl": # or (sibling.name == "div" and sibling.get("class")[0] == "mwe-math-element"):
                    fig = sibling.findAll("img")
                    for f in fig:
                        # print(f.get("alt").strip())
                            alt = f.get("alt")
                            if alt is not None:

                                big_figures.append(alt.strip())
                                section_content.append({"tag":"big_fig_ref", "content":count_big_fig})
                                count_big_fig += 1
                

                                
            ## TODO FIND PICTURES IN LIST

            # Add the section title, content, and images to the hierarchy list
            hierarchy.append({
                "title": section_title,
                "level": heading.name,
                "contents": section_content,
                "images": images_with_captions,
                "tables": tables,
                "big_figures": big_figures
                # "figures": figures
            })
        # print(hierarchy)
        # Print the hierarchy of the article
        # print(hierarchy)
        json_object = json.dumps(hierarchy, indent=4)
        with open("{}.json".format("Wikipedia/" + title + "/" + "slide"), 'w') as outfile:
            # print("writing done")
            outfile.write(json_object)
    except Exception:
        print(title + "error")
        

from multiprocessing import Pool
from multiprocessing import get_context
import tqdm
if not args.related:
    title = args.title
    parse_wiki(title)
else:
    list_articles = {(args.title)}
    new_list_articles = set()
    for el in list_articles:
        print(el)
        wiki = wikipedia.page(el)
        links = wiki.links
        new_list_articles.update(tuple(links))

    new_list_articles.update(list_articles)
    
    # for i in tqdm.tqdm(new_list_articles):
    #     parse_wiki(i)
    new_list_articles = list(new_list_articles)[:args.limit]
    print(new_list_articles)
    pool = get_context("fork").Pool()
    
    # processes = [Process(target=parse_wiki, args=(i,)) for i in new_list_articles]
    for _ in tqdm.tqdm(pool.imap_unordered(parse_wiki, new_list_articles), total=len(new_list_articles)):
        pass
    # for i in sorted(new_list_articles):
    #     pool.apply_async(parse_wiki, args=(i,))
    # pool.close()
    # pool.join()
    
    # for process in processes:
    #     process.start()
    #     # wait for all processes to complete
    # for process in processes:
    #     process.join()
    # report that all tasks are completed
    print('Done', flush=True)


