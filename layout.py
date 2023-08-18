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
                self.addStyle("section::after {content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);}")
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
                
            output.append({"slide": page_output})
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
                output = output + "%i. " % self.count + bp + "\n"            
        return output[:-1] # remove last line return
    def build2(self):
        # output = {"bps":[]}
        output = []
        if self.style == ".":
            for i, bp in enumerate(self.bps):
                # output["bps"].append({"text": bp})
                output.append({"text": "%d. %s" % (self.count, bp)})
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
        self.caption = caption
        self.display_caption = display_caption
    def build(self):
        if self.is_bg:
            option = self.option + "bg " + self.orientation
        if self.width is None:
            # return "![%s](" % self.option + self.img + ")" 
            output = '<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em">\n'
            output = output + "<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0); margin-left:0.1em; margin-right:0.1em' src='{}'/>".format(self.img)
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

def convertToElement(content, bp_style = "-"):
    if content["cls"] == "img":
        return Image(content["image"], caption=content["caption"])
    elif content["cls"] == "text":
        return Text(content["cnt"])
    elif content["cls"] == "bp":
        Page.bps_count += 1
        return BulletPoint([content["cnt"]], style=bp_style, count=Page.bps_count)
def flatten(l):
    return [item for sublist in l for item in sublist]

MAX_NB_IMG = 6
class Page:

    bps_count = 0

    def __init__(self, contents=[]):
        self.contents = contents
        self.style = ""
        self.title = self.generate_title()
        self.body = self.generate_body()
        Page.bps_count = 0
        

    def addPageStyle(self, style):
        self.style = self.style + style

    def generate_title(self):
        return Title(self.contents["title"], True)
    
    def generate_body(self):

        output = []

        # ordered or ul list
        if random.random() > 0.15:
            bp_style = "-"
        else:
            bp_style = "."

        if len(self.contents["text"]) > 0 and random.random() > 0.5:
            self.contents["text"][0]["cls"] = "text"
        txt_elements = [convertToElement(item, bp_style) for item in self.contents["text"]]
        img_elements = [Images([item["image"] for item in self.contents["images"][:MAX_NB_IMG]])]

        
        output.append(txt_elements)
        output.append(img_elements)

        ## adjust text size based on number of elements
        nb_txt_elts = len(txt_elements)
        nb_img_elts = min(len(self.contents["images"]), MAX_NB_IMG)
        self.addPageStyle("p,li {font-size:%.2fem}" % (1.0 - (nb_txt_elts+nb_img_elts)*0.04))

        random.shuffle(output)
        ## BODY CONTENT
        # single column
        if random.random() < 0.66 or nb_img_elts == 0:
            output = flatten(output)
            return output
        else: # double column
            left_c = output[0]
            right_c = output[1]
            return [TwoColumns(left_c, right_c)]

    def build(self):
        output = []
        output.append("<style scoped>%s</style>\n" % self.style)
        output.append(self.title.build())
        for c in self.body:
            output.append(c.build())
        return "\n".join(output)
    def build2(self):
        output = []
        output.append(self.title.build2())
        for c in self.body:
            output.append(c.build2())
        return output

class TitlePage:
    def __init__(self, title="", style = "<!-- _class: lead -->"):
        self.style = style
        self.title = title
    
    def generate_title(self):
        return Title(self.title, True)
    
    def build(self):
        output = []
        output.append("%s\n" % self.style)
        output.append(self.generate_title().build())
        return "\n".join(output)
    
    def build2(self):
        output = []
        output.append(self.generate_title().build2())
        return output

        
