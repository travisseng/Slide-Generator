import json
import random
import re
def parse_content(cnt):
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
            elif line[0] == "+":
                contents.append({"cls":"bp", "lvl":0, "cnt": line.strip().strip("+ ")})
            # elif line[1] == "+":
            #     contents.append({"cls":"bp", "lvl":1, "cnt": line.strip().strip("* ")})
            elif line[:5] == "I hope":
                continue
            elif len(line) > 0:
                contents.append({"cls":"text", "cnt": line.strip()})
        return contents
def parse_contents(contents):
    text_tag = {None, "math-line", "math-inline", "a", "b", "i", "texhtml", "big_fig_ref"}
    text = ""
    for cnt in contents["contents"]:
        if cnt["tag"] in text_tag:
            if cnt["tag"] in {"math-line", "math-inline"}:
                text += "${}$".format(re.sub(r"{\\displaystyle (.*)}", "\g<1>",cnt["content"]).strip())
            elif cnt["tag"] in {"b"}:
                text += "**{}**".format(cnt["content"])
            elif cnt["tag"] == "big_fig_ref":
                text += "\n$${}$$\n".format(re.sub(r"{\\displaystyle (.*?)}", "\g<1>", contents["big_figures"][cnt["content"]]))
            else:
                text += cnt["content"]
    return text
from summa.summarizer import summarize
def parseAll(contents, to_summarize=True, nb_words=40):
    for content in contents:
        if to_summarize:
            content["content"] = [{"cls":"text", "cnt":re.sub(r"\S\*\*(.)\*\*\S", " **\g<1>** ", i)} for i in summarize(parse_contents(content), split=True, words=nb_words)]
        else:
            content["content"] = parse_contents(content)
    return contents
def group_bp_tgt(contents):
    new_contents = []
    bps = {"cls": "bp", "cnt":[]}
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

class Content:
    
    def __init__(self, json_file, article_name = None, summarized=True):
        if article_name is None:
            self.article_name = json_file.split("/")[-2]
        else:
            self.article_name = article_name
        with open(json_file, 'r') as openfile:
            self.contents = json.load(openfile)[1:]
        self.summarized = summarized
        
        if not summarized:
            self.contents = parseAll(self.contents)
        

        
    def getContents(self):
        output = []
        for slide_content in self.contents:
            if not slide_content["content"]:
                continue
            if not self.summarized:
                new_dict = {"title": slide_content["title"], "text": slide_content["content"], "images": [dict(item, **{'cls':'img'}) for item in slide_content["images"]], "equations": slide_content["equations"] if "equations" in slide_content.keys() else [], "tables": slide_content["tables"] if "tables" in slide_content.keys() else []}
            elif "images" in slide_content.keys():
                new_dict = {"title": slide_content["title"], "text": parse_content(slide_content["content"]), "images": [dict(item, **{'cls':'img'}) for item in slide_content["images"]], "equations": slide_content["equations"] if "equations" in slide_content.keys() else [], "tables": slide_content["tables"] if "tables" in slide_content.keys() else []}
                # new_dict = {"title": slide_content["title"], "text": parse_content(slide_content["content"]), "images": [dict(item, **{'cls':'img'}) for item in slide_content["images"]], "equations": [], "tables": slide_content["tables"] if "tables" in slide_content.keys() else []}
            else:
                # new_dict = {"title": slide_content["title"], "text": parse_content(slide_content["content"]), "images": [], "equations": slide_content["equations"] if "equations" in slide_content.keys() else [], "tables": slide_content["tables"] if "tables" in slide_content.keys() else []}
                new_dict = {"title": slide_content["title"], "text": parse_content(slide_content["content"]), "images": [], "equations": [], "tables": slide_content["tables"] if "tables" in slide_content.keys() else []}
            output.append(new_dict)
        return output
    
    def getTitle(self):
        return self.article_name
    
    def getImages(self):
        contents = self.getContents()
        img_list = [item["images"] for item in contents if len(item["images"]) > 0]
        flat_list = [item["image"] for sublist in img_list for item in sublist]
        return flat_list
    
    def getRandomImage(self):
        images = self.getImages()
        if len(images) > 0:
            return random.choice(images)
        else:
            return None
    def getTitles(self):
        return [item["title"] for item in self.contents]
    
    def getRandomTitle(self):
        titles = self.getTitles()
        return random.choice(titles)
    
    def getTables(self):
        contents = self.getContents()
        img_list = [item["tables"] for item in contents if len(item["tables"]) > 0]
        flat_list = [item for sublist in img_list for item in sublist]
        return flat_list

    def getRandomTable(self):
        tables = self.getTables()
        if len(tables) > 0:
            return random.choice(tables)
        else:
            return None