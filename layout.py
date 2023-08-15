import random

class Slide:
    def __init__(self, bg=None, pages = [], paginate = True, style = "") -> None:
        self.background = bg
        self.paginate = paginate
        self.pages = pages
        self.style = style
    def addPage(self, page):
        self.pages.append(page)
    def setTheme(self, theme):
        self.theme = theme
    def setBg(self, bg):
        self.background = bg
    def build(self):
        output = []
        output.append("---")
        output.append("marp: true")
        output.append("math: katex")
        if self.paginate:
            output.append("paginate: True")
        ## style options
        output.append("style: @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css'); %s" % self.style)
        output.append("")
        output.append("---")
        if self.background is not None:
            output = output + self.background.build()
        for i,p in enumerate(self.pages):

            # output.append("\n")
            output.append(p.build())
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

class ColoredBackground:
    # color in string hex or name
    def __init__(self, color) -> None:
        self.color = color
    def build(self):
        return ["<!-- backgroundColor: %s -->" % self.color]
    
class ImageBackground:
    def __init__(self, img) -> None:
        self.img = img
    def build(self):
        return ["<!-- backgroundImage: url('%s') -->" % self.img]
    

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

class Text:
    def __init__(self, text) -> None:
        self.text = text
    def build(self):
        return self.text
    def build2(self):
        return {"text": self.text}


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
        # output = {"bps":[]}
        output = []
        for i, bp in enumerate(self.bps):
            # output["bps"].append({"text": bp})
            output.append({"text": "+ %s" % bp})
        return output


class BlockCode:
    def __init__(self, text, language=None) -> None:
        self.text = text
        self.language = language
    def build(self):
        output = "```%s\n%s\n```" % ("" if self.language is None else 
                                       self.language, self.text)
        return output

    
class Equation:
    def __init__(self, text) -> None:
        self.text = text
    def build(self):
        output = "$$%s$$" % (self.text)
        return output
    
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
            output = output + "<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='{}'/>".format(self.img)
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
    
    def __init__(self, left_contents = [], rights_contents = [], left_c_size=4, right_c_size=4) -> None:
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

def convertToElement(content):
    if content["cls"] == "img":
        return Image(content["image"], caption=content["caption"])
    elif content["cls"] == "text":
        return Text(content["cnt"])
    elif content["cls"] == "bp":
        return BulletPoint([content["cnt"]])
def flatten(l):
    return [item for sublist in l for item in sublist]

class Page:
    def __init__(self, contents=[]):
        self.contents = contents

    def generate_title(self):
        return Title(self.contents["title"], True)
    
    def generate_body(self):

        output = []
        output.append(self.contents["text"])
        output.append(self.contents["images"])
        random.shuffle(output)
        ## BODY CONTENT
        # single column
        if random.random() < 0.66:
            
            output = flatten(output)
            return [convertToElement(item) for item in output]
        else: # double column
            left_c = [convertToElement(item) for item in output[0]]
            right_c = [convertToElement(item) for item in output[1]]
            return [TwoColumns(left_c, right_c)]

    def build(self):
        output = []
        title = self.generate_title()
        body = self.generate_body()
        output.append(title.build())
        for c in body:
            output.append(c.build())
        return "\n".join(output)

        
