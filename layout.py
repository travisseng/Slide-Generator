import random
import numpy as np
class Slide:
    def __init__(self, bg=None, pages = [], paginate = True, theme = "default") -> None:
        self.background = bg
        self.paginate = paginate
        self.paginate_total = False
        self.pages = pages
        self.style = []
        self.theme = theme
        self.header = None
        self.footer = None
    def setHeader(self, header):
        self.header = header
    def setFooter(self, footer):
        self.footer = footer
    def addPage(self, page):
        self.pages.append(page)
    def setTheme(self, theme):
        self.theme = theme
    def setBg(self, bg):
        self.background = bg
    def setPaginate(self, bool, total=False):
        self.paginate = bool
        if total:
            self.paginate_total = True
    def addStyle(self, style):
        self.style.append(style)
    def build(self):
        output = []
        output.append("---")
        output.append("marp: true")
        output.append("math: katex")
        output.append("theme: %s" % self.theme)
        if self.header is not None:
            output.append("header: %s" % self.header)
        if self.footer is not None:
            output.append("footer: %s" % self.footer)
        if self.paginate:

            output.append("paginate: True")
            if self.paginate_total:
                self.addStyle("section::after {height:auto;padding:0;content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);}")
            else:
                self.addStyle("section::after {height:auto;padding:0;bottom:0;}")
        ## style options
        output.append("style: |\n   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');")
        for style in self.style:
            output.append("   %s\n" % style)
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
            page_output = p.build2()
            if self.paginate:
                if self.paginate_total:
                    page_output.append({"page_nb": "%d/%d" % (i+1,len(self.pages))})
                else:
                    page_output.append({"page_nb": i+1})
                
            output.append(page_output)
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
    def __init__(self, colors) -> None:
        self.colors = colors
    def build(self):
        output = []
        output.append("<style>section {background-image: linear-gradient(%s, %s)}</style>" % (self.colors[0], self.colors[1]))
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
                return " ## " + "{}{}{}".format(rand_orn,self.text,rand_orn)
            else:
                return " ## " + self.text
        else:
            return " ## " + self.text
    def build2(self):
        return {"title": self.text}

class Text:
    def __init__(self, text) -> None:
        self.text = text
    def build(self):
        return "\n" + self.text
    def build2(self):
        return {"text": self.text}


class BulletPoint:
    def __init__(self, bps, style="-", count=1, lvl=0):
        self.bps = bps
        self.style = style
        self.lvl = lvl
        self.count = count
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
                output = output + "%i. " % Page.bps_count + bp + "\n"
                Page.bps_count += 1            
        return output[:-1] # remove last line return
    def build2(self):
        # output = {"bps":[]}
        output = []
        if self.style == ".":
            for i, bp in enumerate(self.bps):
                # output["bps"].append({"text": bp})
                output.append({"text": "%d. %s" % (Page.bps_count, bp)})
                Page.bps_count += 1   
        else:
            for i, bp in enumerate(self.bps):
                # output["bps"].append({"text": bp})
                output.append({"text": "+ %s" % (bp)})
        return output


class BlockCode:
    def __init__(self, text, language=None) -> None:
        self.text = text
        self.language = language
    def build(self):
        output = "```%s\n%s\n```" % ("" if self.language is None else 
                                       self.language, self.text)
        return output

import re
class Equation:
    def __init__(self, text) -> None:
        self.text = text
        display_style = re.search(r"{\\displaystyle (.*)}", self.text)
        if display_style is not None:
            self.text = display_style.group(1)
    def build(self):
        output = "$$%s$$" % (self.text)
        return output
    def build2(self):
        # output = {"text": self.text}
        output = {"equation": self.text}
        return output
    
class Image:
    def __init__(self, img, classe = "", caption = "", display_caption=False, is_bg=False, is_header=False, orientation="left", width = None, option = "height:350px", height_percentage=80):
        self.img = img
        self.width = width
        self.is_bg = is_bg
        self.orientation = orientation
        self.option = option
        self.caption = caption
        self.display_caption = display_caption
        self.classe = classe
        self.is_header = is_header
    def build(self):
        if self.is_bg:
            return "![bg contain](%s)" % self.img
        if self.is_header:
            return "<img class='{}' style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='{}'/>\n".format(self.classe,self.img)
        if self.width is None:
            # return "![%s](" % self.option + self.img + ")" 
            output = '<div class="%s" style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em">\n' % self.classe
            output = output + "<img class='{}' style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0); margin-left:0.1em; margin-right:0.1em' src='{}'/>".format(self.classe,self.img)
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

class Table:
    def __init__(self, table, classe = ""):
        self.table = table
        self.classe = classe
    def build(self):
        output = '<div class="%s" style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; overflow:hidden; font-size:0.5em !important;">\n' % self.classe
        output = output + self.table
        output = output + "\n</div>\n"
        return output
    def build2(self):
        # return {"img": self.caption}
        return {"table": ""}

class HorizontalImages:
    def __init__(self, imgs, caption = "", display_caption=False, is_bg=False, orientation="left", width = None, option = "height:350px", height_percentage=80):
        self.imgs = imgs
        self.width = width
        self.is_bg = is_bg
        self.orientation = orientation
        self.option = option
        self.caption = caption
        self.display_caption = display_caption
    def build(self):
        if self.is_bg:
            option = self.option + "bg " + self.orientation
        if self.width is None:
            # return "![%s](" % self.option + self.img + ")"
            output = '<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0">'
            for img in self.imgs:
                output = output + '<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">\n'
            
                output = output + "<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='{}'/>".format(img)
                output = output + "\n</div>\n"
            output = output + "</div>\n"
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
MAX_NB_IMGS_ROW = 3
class Images:
    def __init__(self, imgs):
        self.imgs = imgs
        self.nb_images = len(self.imgs)
    def generate_layout_images(self):
        ## generate image layout based on numbers
        output = []
        nb_rows = int(np.ceil(self.nb_images / MAX_NB_IMGS_ROW))
        for i in range(nb_rows):
            output.append(HorizontalImages(self.imgs[i*MAX_NB_IMGS_ROW:(i+1)*MAX_NB_IMGS_ROW]))
        return output
    def build(self):
        layout_elements = self.generate_layout_images()
        if len(layout_elements) == 0:
            return ""
        output = ""
        
        for el in layout_elements:
            output = output + el.build()
        return output
    def build2(self):
        return [{"img": ""} for item in range(self.nb_images)]

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

class Header:
    def __init__(self, contents) -> None:
        self.contents = contents
    def setContents(self, contents):
        self.contents = contents
    def build(self):
        output = '<header>\n\n'
        for c in self.contents:
            output += c.build() + '\n\n'
        return output + '</header>\n'
    def build2(self):
        output = {"header":[]}
        for c in self.contents:
            output["header"].append(c.build2())
        return output

class Footer:
    def __init__(self, contents) -> None:
        self.contents = contents
    def setContents(self, contents):
        self.contents = contents
    def build(self):
        output = '<footer>\n\n'
        for c in self.contents:
            output += c.build() + '\n'
        return output + '</footer>\n'
    def build2(self):
        output = {"footer":[]}
        for c in self.contents:
            output["footer"].append(c.build2())
        return output


grid_col_7 = Style("<div style='flex:1 1 auto' class=\"grid grid-cols-7 gap-4\">")
grid_col_x = "<div style='flex:1 1 auto; min-height:0;' class=\"grid grid-cols-{} gap-4\">"
col_span_4 = Style("<div class=\"col-span-4\">\n")
col_span_x = "<div style='display:flex; flex-flow:column; min-height:0;' class=\"col-span-{}\">\n"
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
        nb_elements_left = len(self.left_contents)
        # font_size_left = 1.0 - 0.065*nb_elements_left
        ## auto resize depends on number of bullet points
        self.output.append(Style(col_span_x.format(self.left_c_size)))
        self.output = self.output + self.left_contents
        self.output.append(close_div)
        # nb_elements_right = len(self.right_contents)
        # font_size_right = 1.0 - 0.065*nb_elements_right
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
        output = []
        for cnt in self.left_contents:
            output.append(cnt.build2())
        for cnt in self.right_contents:
            output.append(cnt.build2())
        return output

class Columns:
    
    def __init__(self, contents = [[]], c_size=[3,3,3]) -> None:
        self.contents = contents
        self.c_size = c_size
        self.output = []
    def build(self):
        self.output.append(Style(grid_col_x.format(np.sum(self.c_size))))
        for i,col in enumerate(self.contents):
            self.output.append(Style(col_span_x.format(self.c_size[i])))
            self.output = self.output + col
            self.output.append(close_div)
        # nb_elements_right = len(self.right_contents)
        # font_size_right = 1.0 - 0.065*nb_elements_right
        self.output.append(close_div)
        o = []
        for c in self.output:
            # print(c)
            o.append(c.build())
        return "\n".join(o)
    def build2(self):
        output = []
        for col in self.contents:
            for cnt in col:
                output.append(cnt.build2())
        return output
    
def convertToElement(content, bp_style = "-"):
    if content["cls"] == "img":
        return Image(content["image"], caption=content["caption"])
    elif content["cls"] == "text":
        return Text(content["cnt"])
    elif content["cls"] == "bp":
        
        return BulletPoint([content["cnt"]], style=bp_style, count=Page.bps_count)
def flatten(l):
    return [item for sublist in l for item in sublist]

MAX_NB_IMG = 6
MAX_NB_EQUATIONS = 3
class Page:

    bps_count = 0

    def __init__(self, contents=[], display_title=True, title=None, header=None, footer=None):
        self.contents = contents
        self.display_title = display_title
        self.style = ""
        if title is None:
            self.title = self.generate_title()
        else:
            self.title = self.generate_title(title)
        self.body = self.generate_body()
        self.header = header
        self.footer = footer
        Page.bps_count = 0
    
    def setHeader(self, header):
        self.header = header

    def setFooter(self, footer):
        self.footer = footer

    def setDisplayTitle(self, display):
        self.display_title = display
    def addPageStyle(self, style):
        self.style = self.style + style

    def generate_title(self, title=None):
        if title is None:
            return Title(self.contents["title"], True)
        else:
            return Title(title)
    
    def generate_body(self):

        output = []
        if self.contents == []:
            return []
        # ordered or ul list
        if random.random() > 0.15:
            bp_style = "-"
        else:
            bp_style = "."
        # transform to text randomly
        if len(self.contents["text"]) > 0 and random.random() > 0.5:
            for i in range(len(self.contents["text"])):
                if random.random() > 0.5: 
                    self.contents["text"][i]["cls"] = "text"
        
        txt_elements = [convertToElement(item, bp_style) for item in self.contents["text"]]
        img_elements = [Images([item["image"] for item in self.contents["images"][:MAX_NB_IMG]])]
        figures_elements = self.contents["equations"] if "equations" in self.contents.keys() else []





        ## adjust text size based on number of elements
        nb_txt_elts = len(txt_elements)
        nb_img_elts = min(len(self.contents["images"]), MAX_NB_IMG)

        
        self.addPageStyle("p,li {font-size:%.2fem}" % (1.0 - (nb_txt_elts+nb_img_elts)*0.04))

        ## add elements
        output.append(txt_elements)
        if nb_img_elts > 0:
            output.append(img_elements)
        if len(figures_elements) > 0:
            random.shuffle(figures_elements)
            output.append([Equation(item) for item in figures_elements[:MAX_NB_EQUATIONS]])

        random.shuffle(output)
        ## BODY CONTENT
        # single column
        prob = random.random()
        if prob < 0.5:
            output = flatten(output)
            return output
        elif prob < 0.93: # double column
            output = flatten(output)
            random.shuffle(output)
            half = len(output) // 2

            # left_c = output[0]
            # right_c = output[1]
            return [Columns([output[:half], output[half:]], c_size=[3,3])]
        else: # double column
            output = flatten(output)
            random.shuffle(output)
            third = len(output) // 3
            # left_c = output[0]
            # right_c = output[1]
            return [Columns([output[:third], output[third:third+1], output[third+1:]], c_size=[3,3, 3])]

    def build(self):
        Page.bps_count = 1
        output = []
        output.append("<style scoped>%s</style>\n" % self.style)
        if self.header is not None:
            output.append(self.header.build())
        if self.footer is not None:
            output.append(self.footer.build())
        if self.display_title:
            output.append(self.title.build())
            
        for c in self.body:
            output.append(c.build())
        return "\n".join(output)
    def build2(self):
        Page.bps_count = 1   
        output = []
        if self.header is not None:
            output.append(self.header.build2())
        body = []
        if self.display_title:
            body.append(self.title.build2())
        for c in self.body:
            body.append(c.build2())
        output.append({'body' : body})
        if self.footer is not None:
            output.append(self.footer.build2())
        return output

class TitlePage:
    def __init__(self, title="", content=[], header=None, footer=None, style = "<!-- _class: lead -->"):
        self.style = style
        self.content = content
        self.title = title
        self.header = header
        self.footer = footer
    
    def generate_title(self):
        return Title(self.title, True)

    def setHeader(self, header):
        self.header = header

    def setFooter(self, footer):
        self.footer = footer

    def addPageStyle(self, style):
        self.style = self.style + style

    def build(self):
        output = []
        self.addPageStyle("<style scoped>p,li {font-size:%.2fem}</style>" % (1.0 - len(self.content)*0.04))
        if self.header is not None:
            output.append(self.header.build())
        if self.footer is not None:
            output.append(self.footer.build())       
        output.append("%s\n" % self.style)
        output.append(self.generate_title().build())
        for c in self.content:
            output.append(c.build())
        return "\n".join(output)
    
    def build2(self):
        output = []
        if self.header is not None:
            output.append(self.header.build2())
        body = [self.generate_title().build2()]
        for c in self.content:
            body.append(c.build2())
        output.append({"body": body})
        if self.footer is not None:
            output.append(self.footer.build2())
        return output

class ImagePage:
    def __init__(self, img, title=None, is_bg=False, header=None, footer=None):
        self.img = img
        self.is_bg = is_bg
        self.img_elt = Image(self.img, is_bg=is_bg)
        self.title = title
        self.body = self.generateBody()
        self.header = header
        self.footer = footer

    def generateBody(self):
        body = []
        if self.title is not None:
            body.append(Title(self.title))
        body.append(self.img_elt)
        random.shuffle(body)
        return body

    def setHeader(self, header):
        self.header = header
    
    def hasHeader(self):
        return self.header is not None

    def setFooter(self, footer):
        self.footer = footer

    def hasFooter(self):
        return self.footer is not None
        
    def build(self):
        output = []
        if self.header is not None:
            output.append(self.header.build())
        if self.footer is not None:
            output.append(self.footer.build())
        for c in self.body:
            output.append(c.build())
        return "\n".join(output)
    
    def build2(self):
        output =  []
        if self.header is not None:
            output.append(self.header.build2())
        body = {"body": []}
        for c in self.body:
            body["body"].append(c.build2())
        output.append(body)
        if self.footer is not None:
            output.append(self.footer.build2())
        return [output]
        
