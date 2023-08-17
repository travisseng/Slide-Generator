# from essential_generators import DocumentGenerator
# from wonderwords import RandomWord, RandomSentence
# from utils import random_code
import random
import argparse
import subprocess
random.seed(0)
list_fonts = subprocess.check_output(['fc-list', ':lang=en']).decode('utf-8').split(":")[1::2]
print(list_fonts)
themes = ["academic", "default", "gaia", "uncover"]
class Slide:
    def __init__(self, bg=None, color='', contents=[], header = "", footer = "", paginate = True, theme = "default", color_styles = "") -> None:
        self.background = bg
        self.color = color
        self.header = header
        self.footer = footer
        self.paginate = paginate
        self.theme = theme
        self.pages = [[]]
        self.current_page = 0
        self.style = ""
        self.color_styles = color_styles
    def addContent(self, content):
        self.pages[self.current_page].append(content)
    def addContents(self, contents):
        for c in contents:
            self.pages[self.current_page].append(c)
    def addHeader(self, header):
        self.header = header
    def addFooter(self, footer):
        self.footer = footer
    def setTheme(self, theme):
        self.theme = theme
    def newPage(self):
        self.current_page += 1
        self.pages.append([])
    def popPage(self):
        self.current_page -= 1
        self.pages = self.pages[:-1]
    def setBg(self, bg):
        self.background = bg
    def addStyle(self, style):
        self.style = self.style + style
    def build(self):
        output = []
        output.append("---")
        output.append("marp: true")
        output.append("math: katex")
        if self.theme != "":
            output.append("theme: %s" % self.theme)
        if self.header != "":
            output.append("header: %s" % self.header)
        if self.footer != "":
            output.append("footer: %s" % self.footer)
        if self.paginate:
            output.append("paginate: False")
        if self.color != "":
            output.append("color: %s" % self.color)
        # output.append("---")
        ## style options
        output.append("style: @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');section { font-size: %dpx; font-family: '%s'; display: flex;flex-flow: column nowrap;} table {font-size: 0.5em} %s" % (random.randint(24,32), random.choice(list_fonts).strip(), self.style))
        output.append("")
        output.append("---")
        if self.background is not None:
            output = output + self.background.build()
        
        output.append(self.color_styles)
        for i,p in enumerate(self.pages):
            
            # output.append('<div style="height: 100%; max-height: 100vh; margin: 0px; padding: 0px;display:flex;flex-flow:column nowrap;";>')
            output.append("\n")
            for c in p:
                output.append(c.build())
            # output.append('</div>')
            if i < len(self.pages) - 1:
                output.append("")
                output.append("---")
        try:
            return "\n".join(output)
        except:
            print(output)
            raise Exception()
    def build2(self):
        output = []
        for i,p in enumerate(self.pages):
            output.append({"slide": []})
            for c in p:
                if c.build2() is not None:
                    output[i]["slide"].append(c.build2())
        return output
    def get_tag(self):
        fullTag = self.background.get_tag()
        if self.header != "":
            fullTag = fullTag + "_H"
        if self.footer != "":
            fullTag = fullTag + "_F"
        for c in self.pages[0]:
            fullTag = fullTag + "_" + c.get_tag()
        return fullTag
    def setColor(self, color):
        self.color = color
    def setColorStyles(self, color_styles):
        self.color_styles = color_styles


class ColoredBackground:
    # color in string hex or name
    def __init__(self, color) -> None:
        self.color = color
    def build(self):
        return ["<!-- backgroundColor: %s -->" % self.color]
    def get_tag(self):
        return "%sBg" % self.color

class ImageBackground:
    def __init__(self, img) -> None:
        self.img = img
    def build(self):
        return ["<!-- backgroundImage: url('%s') -->" % self.img]
    def get_tag(self):
        return "imgBg"
    

class GradientBackground:
    def __init__(self, deg = 180) -> None:
        self.deg = int(deg)
    def build(self):
        output = []
        output.append("<style>")
        output.append("section {")
        output.append("background: rgb(0,0,0);")
        output.append("background: linear-gradient({0}deg, rgba(0,0,0,1) 0%, rgba(255,255,255,1) 100%);".format(self.deg))
        output.append("}")
        output.append("</style>")
        return output
    def get_tag(self):
        return "gradientBg"

class CheckerBackground:
    def build(self):
        output = []
        output.append("<style>")
        output.append("section {")
        output.append("background-position: 0px 0px, 10px 10px;")
        output.append("background-size: 20px 20px;")
        output.append("background-image: linear-gradient(45deg, #eee 25%, transparent 25%, transparent 75%, #eee 75%, #eee 100%),linear-gradient(45deg, #eee 25%, white 25%, white 75%, #eee 75%, #eee 100%);")
        output.append("}")
        output.append("</style>")
        return output
    def get_tag(self):
        return "checkerBg"

ornement = ["_", "**"]
class Title:
    def __init__(self, text, rand=False) -> None:
        self.text = text
        self.rand = rand
    def build(self):
        if self.rand:
            if random.random() > 0.7:
                rand_orn = random.choice(ornement)
                return " # " + "{}{}{}".format(rand_orn,self.text,rand_orn)
            else:
                return " # " + self.text
        else:
            return " # " + self.text
    def build2(self):
        return {"title": self.text}
    def get_tag(self):
        return "title"
    
class Text:
    def __init__(self, text) -> None:
        self.text = text
    def build(self):
        return self.text
    def build2(self):
        return {"text": self.text}
    def get_tag(self):
        return "p"

class BulletPoint:
    def __init__(self, bps, style="-", lvl=0):
        self.bps = bps
        self.style = style
        self.lvl = lvl
    def build(self):
        output = ""
        if self.style == "-":
            for i, bp in enumerate(self.bps):
                for i in range(self.lvl):
                    output = output + " "
                output = output + "- " + bp + "\n"
        elif self.style == ".":
            for i, bp in enumerate(self.bps):
                for i in range(self.lvl):
                    output = output + " "
                output = output + "%i. " % i + bp + "\n"            
        return output
    def build2(self):
        output = {"bps":[]}
        for i, bp in enumerate(self.bps):
            output["bps"].append({"text": bp})
        return output
    def get_tag(self):
        return "bp"

class BlockCode:
    def __init__(self, text, language=None) -> None:
        self.text = text
        self.language = language
    def build(self):
        output = "```%s\n%s\n```" % ("" if self.language is None else 
                                       self.language, self.text)
        return output
    def get_tag(self):
        return "bC"
    
class Equation:
    def __init__(self, text) -> None:
        self.text = text
    def build(self):
        output = "$$%s$$" % (self.text)
        return output
    def get_tag(self):
        return "EQ"
    
class Image:
    def __init__(self, img, classe = "", caption = "", display_caption=False, is_bg=False, orientation="left", width = None, option = "height:350px", height_percentage=80):
        self.img = img
        self.width = width
        self.is_bg = is_bg
        self.orientation = orientation
        self.option = option
        self.height_percentage = height_percentage
        self.caption = caption
        self.display_caption = display_caption
    def build(self):
        if self.is_bg:
            option = self.option + "bg " + self.orientation
        if self.width is None:
            # return "![%s](" % self.option + self.img + ")" 
            output = '<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em">\n'
            output = output + "<img style='object-fit: contain; align-self: center; max-height:100%; max-width:100%' src='{}'/>".format(self.img)
            output = output + "\n</div>\n"
            if self.caption != "" and self.display_caption == True:
                # print(self.caption)
                # output = output + '\n <p style="text-align: center;">%s</p>' % self.caption
                output = output + "\n \n" + self.caption
            return output
    def build2(self):
        # return {"img": self.caption}
        return {"img": ""}
    def setDisplayCaption(self, bool):
        self.display_caption = bool
    def setHeightPercentage(self, height_percentage):
        self.height_percentage = height_percentage
    def get_tag(self):
        return "img"

class HorizontalLayout:
    def __init__(self, contents = []) -> None:
        self.contents = contents
    def addContent(self, cnt):
        self.contents.append(cnt)
    def build(self):
        output = ""
        for c in self.contents:
            output += "%s " % c.build()
        return output
    def get_tag(self):
        fullTag = "HL"
        for c in self.contents:
            fullTag = fullTag + "_" + c.get_tag()
        fullTag = fullTag + "_"
        return fullTag
        
class Style:
    def __init__(self, option="") -> None:
        self.option = option
    def build(self):
        return self.option
    def build2(self):
        return None
    
class HtmlElement:
    def __init__(self, html) -> None:
        self.html = html
    def build(self):
        return self.html + "\n"
    def build2(self):
        return ""

grid_col_7 = Style("<div style='flex:1 1 auto' class=\"grid grid-cols-7 gap-4\">")
grid_col_x = "<div style='flex:1 1 auto; min-height:0' class=\"grid grid-cols-{} gap-4\">"
col_span_4 = Style("<div class=\"col-span-4\">\n")
col_span_x = "<div style='display:flex; flex-flow:column; min-height:0' class=\"col-span-{}\">\n"
close_div = Style("</div>\n")
col_span_3 = Style("<div class=\"col-span-3\">\n")

class TwoColumns:
    def __init__(self, left_contents = [], rights_contents = [], left_c_size=4, right_c_size=3) -> None:
        self.left_contents = left_contents
        self.right_contents = rights_contents
        self.left_c_size = left_c_size
        self.right_c_size = right_c_size
        self.output = []
    def build(self):
        self.output.append(Style(grid_col_x.format(self.left_c_size + self.right_c_size)))
        self.output.append(Style(col_span_x.format(self.left_c_size)))
        self.output = self.output + self.left_contents
        self.output.append(close_div)
        self.output.append(Style(col_span_x.format(self.right_c_size)))
        self.output = self.output + self.right_contents
        self.output.append(close_div)
        self.output.append(close_div)
        o = []
        for c in self.output:
            # print(c)
            o.append(c.build())
        return "\n".join(o)
    def build2(self):
        return None
        
def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def parse_text(contents):
    text_tag = {None, "math-line", "math-inline", "a", "b", "texhtml"}
    text = ""
    for cnt in contents:
        
        if cnt["tag"] in text_tag:
            if cnt["tag"] in {"math-line", "math-inline"}:
                text += "${}$".format(cnt["content"])
            elif cnt["tag"] in {"b", "a"}:
                # text += "**{}**".format(cnt["content"])
                text += "{}".format(cnt["content"])
            else:
                text += cnt["content"]
    return text

def parse_list(list):
    el_text = [parse_text(cnt) for cnt in list["content"]]
    nb_elements = len(el_text)
    # print(el_text)
    
    bps = BulletPoint(el_text[:min(nb_elements,random.randint(1,4))], "-" if list["tag"] == "ul" else ".")
    return bps

def layout(sli, sentences, lists, big_figures, images, codes, tables):
    ## base layout
    # sli.addContent(Title(title))
    if len(images) > 0:
        img = random.choice(images)
        images.remove(img)
        img.setHeightPercentage(75)
        img.setDisplayCaption(True)
        sli.addContent(img)
        sli.newPage()
    
    random_sentences = random.sample(sentences, random.randint(1, min(len(sentences), 1))) if len(sentences) > 0 else []
    random_lists = random.sample(lists, random.randint(1, min(len(lists), 2))) if len(lists) > 0 else []
    random_big_figures = random.sample(big_figures, random.randint(1, min(len(big_figures), 2))) if len(big_figures) > 0 else [] 
    random_codes = random.sample(codes, random.randint(1, min(len(codes), 2))) if len(codes) > 0 else []
    random_images = random.sample(images, random.randint(2 if len(images) > 1 else 1, min(len(images), 5))) if len(images) > 0 else []
    for im in random_images:
        im.setDisplayCaption(False)
    random_tables = random.sample(tables, random.randint(1, min(len(tables), 2))) if len(tables) > 0 else []
    if len(images) > 0:
        if random.random() > 0.5:
            sli.addContent(TwoColumns((random_sentences + random_lists), random_images, random.randint(2,5), random.randint(2,5)))
        else:
            sli.addContent(TwoColumns(random_images, (random_sentences + random_lists), random.randint(2,5), random.randint(2,5)))
    else:
        sli.addContents(random_sentences + random_lists)
    if len(random_big_figures) > 0:
        sli.addContents(random_big_figures)
    if len(random_codes) > 0:
        sli.newPage()
        sli.addContent(random_codes[0])
    if len(random_tables) > 0:
        sli.newPage()
        sli.addContents(random_tables)
    

    # sli.addContents(random_sentences)
    return

import glob

WHITE = (1, 1, 1)
BLACK = (0, 0, 0)
GRAY = (0.5,0.5,0.5)

images_bg = glob.glob("bg_images/*")
images_wall = glob.glob("wallpapers/*/*.jpg") + glob.glob("wallpapers/*/*.png")
parser = argparse.ArgumentParser(description="Wikislide parser")
parser.add_argument("--title", dest="title", type=str, default="Toulouse", help="Name of the article")
args = parser.parse_args()
# Set the language of the Wikipedia page
# Set the title of the Wikipedia page
article_title = args.title
import json
import os
import distinctipy
import numpy as np
from multiprocessing import Process  
colors = distinctipy.get_colors(36,[WHITE,BLACK], pastel_factor=0.7)
import cv2
import colorsys

# def parse_content(cnt):
#     ## detect type
#     if len(cnt) < 1:
#         return None, None
#     elif cnt[:7] == "* Title":
#         text_index = cnt.find("Text:")
#         # Get the substring after "Text:"
#         if text_index != -1:
#             text = cnt[text_index + len("Text:"):].strip()
#             # text = re.findall(r"Text: (.+)", text)
#             text = [item.strip().strip('"').strip("* ") for item in text.split('\n') if len(item.strip('* ').strip()) > 0]
#             return text, "text"
#         else:
#             return None, None
#     elif cnt[0] == "*": # bullet point style
#         bps = [item.strip("* ") for item in cnt.split('\n') if len(item.strip('* ').strip()) > 0]
#         return bps, "bp"
#     else:
#         return None, None

def parse_content(cnt):
    ## detect type
    lines = [item.strip() for item in cnt.split('\n') if len(item.strip()) > 0]
    contents = []
    for line in lines:
        line = line.strip("-")
        if len(line) == 0:
            continue
        elif line[:7] == "* Title":
            text_index = cnt.find("Text:")
            if text_index != -1:
                text = cnt[text_index + len("Text:"):].strip()
                text = text.strip().strip("* ")
                contents.append({"cls":"text", "cnt": text})
        elif line[0] == "*":
            contents.append({"cls":"bp", "lvl":0, "cnt": line.strip().strip("* ")})
        elif line[1] == "+":
            contents.append({"cls":"bp", "lvl":1, "cnt": line.strip().strip("* ")})
        elif line[:5] == "I hope":
            continue
        elif len(line) > 0:
            contents.append({"cls":"text", "cnt": line.strip()})
    return contents

def group_bp_tgt(contents):
    new_contents = []
    bps = {"cls": "bp", "cnt":[]}
    current_lvl = 0
    for i in range(len(contents)):
        if contents[i]["cls"] == "bp" and i < len(contents) - 1:
            bps["cnt"].append(contents[i]["cnt"])
            bps["lvl"] = contents[i]["lvl"]

        else:
            if contents[i]["cls"] == "bp":
                bps["cnt"].append(contents[i]["cnt"])
                bps["lvl"] = contents[i]["lvl"]
            if len(bps["cnt"]) > 0:
                new_contents.append(bps)
                bps = {"cls": "bp", "cnt":[]}
            if contents[i]["cls"] != "bp":
                new_contents.append(contents[i])
    return new_contents
        
            

    
def generate_slide(filename):

    article_title = filename
    # print(article_title)
    try:
        with open("output/{}/{}.json".format(article_title, "sum_slide"), 'r') as openfile:
            json_obj = json.load(openfile)
            sli = Slide()
            main_title = article_title
            # if random.random() < 0.3:
            #     sli.addHeader(main_title)
            random_theme = random.choice(themes)
            sli.setTheme(random_theme)
            if random_theme != "beamer":
                two_colors = random.sample(colors, 11)
                # print()
                random_font_size = random.randint(6,9)
                sli.addStyle("footer {font-size:0.%dem;}" % (random_font_size))
                img_bg = random.choice(images_bg)
                img_wall = random.choice(images_wall)
                
                bg_style = ""
                random_for_bg = random.random()
                black_or_white = (0,0,0)
                if random_for_bg > 0.8:
                    random_transparency = random.uniform(0.6,1)
                    bg_style = "<style>section {background-image: linear-gradient(rgba(255,255,255,%1f), rgba(255,255,255,%1f)), url('%s');background-size: cover;background-clip: content-box, border-box;}</style>" % (random_transparency, random_transparency, "../../" + img_wall)
                elif random_for_bg > 0.7:
                    sli.setBg(ImageBackground("../../" + img_bg))
                    luminance = np.mean(cv2.cvtColor(cv2.imread(img_bg), cv2.COLOR_BGR2HSV)[:,:,2])/255.0
                    if luminance > 0.5:
                        black_or_white = (0,0,0)
                    else:
                        black_or_white = (1,1,1)
                elif random_for_bg > 0.55:
                    bg_style = "<style>section {background-image: linear-gradient(%s, %s)}</style>" % (distinctipy.get_hex(two_colors[9]), distinctipy.get_hex(two_colors[10]))
                elif random_for_bg > 0.5:
                    sli.setBg(ColoredBackground(distinctipy.get_hex(two_colors[0])))
                else:
                    sli.setBg(ColoredBackground(distinctipy.get_hex((1,1,1))))
                    black_or_white = (0,0,0)
                    
                if random_theme == "academic":
                    sli.addStyle("header {background-color: %s;}" % distinctipy.get_hex(two_colors[1]))
                if random_theme == "uncover":
                    sli.addStyle("section  {padding:70px;}")
                # sli.setBg(GradientBackground())
                
                txt_color = distinctipy.get_hex(black_or_white)
                color_styles = "<style>:root {--color-fg-default: %s;--color-background-paginate:%s;--color-foreground: %s;--color-highlight: %s;--color-highlight-heading: %s;--color-header: %s;--color-header-shadow: transparent;--color-dimmed: %s;}</style>" % (txt_color,distinctipy.get_hex(two_colors[3]),
                            txt_color,distinctipy.get_hex(two_colors[5]),
                            distinctipy.get_hex(two_colors[6]),distinctipy.get_hex(two_colors[7]),distinctipy.get_hex(two_colors[8]))
                
                

                sli.setColorStyles(bg_style + color_styles)
            # TODO add title slide
            
            for i, h in enumerate(json_obj[1:]):
                content_json = h["content"]
                # print(len(contents))
                nb_images = 0
                title = h["title"]
                parsed_content_dict = parse_content(content_json)
                parsed_content_dict = group_bp_tgt(parsed_content_dict)
                text = ""
                # text = parsed_content
                
                mirror_img = random.random() > 0.5
                if "images" in h.keys():
                    images = h["images"]
                    
                    nb_images = len(images) if images is not None else 0
                    select_img_nb = 1 if nb_images == 0 else random.randint(1, nb_images)
                    imgs = [Image(img["image"], caption=parse_text(img["caption"]), height_percentage=75//select_img_nb) for img in images]
                    
                
                # add title
                if title in {"See also", "References", "External links"}:
                    sli.popPage()
                    break
                if len(parsed_content_dict) < 1 and nb_images == 0:
                    if random_theme == "beamer":
                        sli.addContent(Style("<!-- _class: title -->"))
                    else:
                        sli.addContent(Style("<!-- _class: lead -->"))
                    sli.addContent(Title(title, True))
                    sli.newPage()
                    continue
                else:
                    sli.addContent(Title(title, True))

                # if "images" in h.keys() and mirror_img:
                #     sli.addContents(imgs)
                for item in parsed_content_dict:
                    if item["cls"] == "text":
                        text_content = Text(item["cnt"])
                        
                    elif item["cls"] == "bp":
                        
                        text_content = BulletPoint(item["cnt"],lvl=item["lvl"])
                # sli.addContent(text_content)
                # twocols = TwoColumns(text_content, imgs)
                if "images" in h.keys(): # and not mirror_img:
                    # sli.addContents(imgs)
                    sli.addContent(TwoColumns([text_content], imgs))
                else:
                    sli.addContent(text_content)
                # twocols = TwoColumns([Text(sentences[0])] + lists, imgs)

                

                
                #

                # print(nb_sentences)
                ## create bps
                ## check images
                
                
                # twocols = TwoColumns([Text(sentences[0])] + lists, imgs)

                # layout(sli, sentences, lists, big_figures, imgs, codes, tables)
                ## pick random sentences and bp
                # if sentences > 


                # sli.addContent(twocols)
                # sli.addContents(codes)
                # sli.addContents(tables)
                # print("i", i)
                # print(len(json_obj))
                if i != len(json_obj)-1:
                    sli.newPage()

                
            with open("output/{}/{}.md".format(article_title, "slide"), "w") as f:
                print(article_title + " done")
                f.write(sli.build()[:-5])
                
            with open("output/{}/output2.json".format(article_title), "w") as f:

                json_data = json.dumps(sli.build2())
                f.write(json_data)
            sli = None
    except (FileNotFoundError):
        print(article_title + " doesn't exist")
# sli = Slide(ColoredBackground("white"))

sum_slide_jsons = sorted(glob.glob("/home/tseng/projects/slide_generator/output/*/sum_slide.json"))
sum_slide_jsons_article_name = list(map(lambda x: x.split("/")[-2], sum_slide_jsons))
# for i in sum_slide_jsons_article_name:
#     generate_slide(i)
processes = [Process(target=generate_slide, args=(i,)) for i in sum_slide_jsons_article_name]
for process in processes:
    process.start()
    # wait for all processes to complete
for process in processes:
    process.join()
# report that all tasks are completed
print('Done', flush=True)