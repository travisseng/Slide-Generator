from content import Content
from layout import Page, TitlePage, Slide, ImageBackground, ColoredBackground, GradientBackground, ImagePage, Header, Title, Text, Image
import json
import random
import glob
import cv2
import numpy as np
import distinctipy
import randomcolor
rand_color = randomcolor.RandomColor()
bullet_styles = [r"\2022", r"\2299", r"\229A", r"\229B", r"\25C9", r"\29BF", r"\29BE", r"\25C6", r"\25C7", r"\25C8", r"\2731", r"\2724", r"\2732", r"\2726", r"\2727", r"\25A0", r"\2612", r"\25A1", r"\2713", r"\2714", r"\27A2", r"\27A3", r"\27A4", r"\27AE", r"\27B1", r"\25B7", r"\25B8", r"\25B9", r"\25BA", r"\25BB"]


FONT_SIZE = (29,35)
LETTER_SPACING = (1.3,1.4)
LINE_HEIGHT = (1.1,1.4)
PROB_DISPLAY_TITLE = 0.8
PROB_HEADER = 0.35
PADDING_RANGE = (80,105)
LOGOS_FILES = glob.glob("Logos/*.png") + glob.glob("Logos/*.jpg") + glob.glob("Logos/*.gif")
border_styles = ["dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]

def generateHeaderStyle(prob_bg=0.5,prob_border=0.5):
    style_choice = ""
    margin = 0
    if random.random() < prob_bg:
        style_choice += "background-color: {};color: #000;" .format(rand_color.generate(luminosity= 'light')[0])
    else:
        margin = random.randrange(0,15)
        style_choice += "border-bottom-style: {}; border-width: {}px; border-color:{};".format(random.choice(border_styles), random.randrange(4,8), rand_color.generate(luminosity= 'light')[0])
    padding_top = random.randrange(PADDING_RANGE[0],PADDING_RANGE[1])
    style = "left: {}%; right: {}%;top: 0;  box-sizing: border-box;font-size: 66%; height: {}px;line-height: 50px;padding: 10px 25px;position: absolute;font-size: 1em;font-weight: 700; display:flex; {}".format(margin, margin, padding_top,style_choice)

    # style = ""
    return style, padding_top
        
def createSlide(json_file, name=None):
    ## output : slide markdown, slide json (for pix2struct for example)
    if name is not None:
        c = Content(json_file, name)
    else:
        c = Content(json_file)

    # Create header
    hasHeader = random.random() < PROB_HEADER
    # Create layout
    title_page = TitlePage(c.getTitle())
    titles = c.getTitles()
    pages = [Page(item, display_title=random.random() < PROB_DISPLAY_TITLE, title=title) for item, title in zip(c.getContents(), titles)]

    padding_top = None
    if hasHeader:
        styleHeader, padding_top = generateHeaderStyle()
        for i, p in enumerate(pages):
            if random.random() < 0.3:
                p.setDisplayTitle(False)
                header_content = [Title(titles[i])]
                if random.random() > 0.5:
                    header_content.append(Image("../../" + random.choice(LOGOS_FILES), classe="logo",is_header=True))
                    random.shuffle(header_content)
                p.setHeader(Header(header_content))
            else:
                p.setHeader(Header([]))
    list_pages = [title_page] + pages
    # add random image slide for diversity
    random_image = c.getRandomImage()
    if random_image is not None:
        list_pages += [ImagePage(c.getRandomImage(), is_bg=random.random() > 0.5) for i in range(2)]
    
    random.shuffle(list_pages)
    sli = Slide(pages=list_pages)

    # Customize template and style
    ## Paginate
    if random.random() > 0.2:
        if random.random() > 0.4:
            sli.setPaginate(True,total = False)
        else:
            sli.setPaginate(True, total = True)
    else:
        sli.setPaginate(False)

    ## BACKGROUND
    bg_prob = random.random()
    if bg_prob > 0.6:
        # Get white background
        sli.setBg(ColoredBackground("white"))
    elif bg_prob > 0.5:
        # Get colored background
        sli.setBg(ColoredBackground(distinctipy.get_hex(distinctipy.get_colors(1, pastel_factor=1)[0])))
    elif bg_prob > 0.4:
        # Get colored background
        sli.setBg(GradientBackground([distinctipy.get_hex(distinctipy.get_colors(1, pastel_factor=1)[0]), "#FFFFFF"]))
    else:
        # Get random background
        backgrounds = glob.glob("backgrounds/*.png")
        bg = random.choice(backgrounds)
        luminance = np.mean(cv2.cvtColor(cv2.imread(bg), cv2.COLOR_BGR2HSV)[:,:,2])/255.0
        if luminance < 0.5:
            sli.addStyle(":root {--color-fg-default: %s; --color-foreground: %s;}" % ("#FFFFFF", "#FFFFFF"))
        sli.setBg(ImageBackground("../../" + bg))

    ## THEME
    # select random theme
    themes = ["default", "uncover", "gaia"]
    sli.setTheme(random.choice(themes))

    # Header related
    header_style = ""
    header_related = ""
    if hasHeader:
        header_style = styleHeader
        header_related = "padding-top: %dpx;" % (padding_top + 10)
    sli.addStyle("header {overflow:visible; color: inherit; %s}" % header_style)
    # sli.addStyle("header > div.logo {position:absolute; top: 0px; right:15px; height: 75px;}")
    sli.addStyle("header > * {margin: 0 0 0; margin: auto;}")

    ## Style
    # Section related
    sli.addStyle("section {display: flex;flex-flow: column; font-size:%.3fpx; letter-spacing:%.3fpx; line-height: %.3f; %s}" % (random.uniform(FONT_SIZE[0],FONT_SIZE[1]), random.uniform(LETTER_SPACING[0], LETTER_SPACING[1]), random.uniform(LINE_HEIGHT[0], LINE_HEIGHT[1]), header_related))


    # Bullet point related
    sli.addStyle("ul > li::marker {content: '%s  ';}" % random.choice(bullet_styles))
    return sli.build(), sli.build2()

if __name__ == "__main__":
    sli_md, sli_json = createSlide("/home/travis/Documents/these/projects/Slide-Generator/sum_slide.json", "Photography")
    with open("test.md", "w") as f:
        f.write(sli_md)
    with open("test.json", "w") as f:
        f.write(json.dumps(sli_json))