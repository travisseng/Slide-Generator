import json

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
    
    def __init__(self, json_file, article_name = None):
        if article_name is None:
            self.article_name = json_file.split("/")[-2]
        else:
            self.article_name = article_name
        with open(json_file, 'r') as openfile:
            self.contents = json.load(openfile)[1:]
        
    def getContents(self):
        output = []
        for slide_content in self.contents:
            if "images" in slide_content.keys():
                new_dict = {"title": slide_content["title"], "text": parse_content(slide_content["content"]), "images": [dict(item, **{'cls':'img'}) for item in slide_content["images"]]}
            else:
                new_dict = {"title": slide_content["title"], "text": parse_content(slide_content["content"]), "images": []}
            output.append(new_dict)
        return output
    
    def getTitle(self):
        return self.article_name