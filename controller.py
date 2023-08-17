from content import Content
from layout import Page, TitlePage, Slide, ImageBackground, ColoredBackground, GradientBackground
import json
import random
import glob
import cv2
import numpy as np
import distinctipy

bullet_styles = [r"\2022", r"\2299", r"\229A", r"\229B", r"\25C9", r"\29BF", r"\29BE", r"\25C6", r"\25C7", r"\25C8", r"\2731", r"\2724", r"\2732", r"\2726", r"\2727", r"\25A0", r"\2612", r"\25A1", r"\2713", r"\2714", r"\27A2", r"\27A3", r"\27A4", r"\27AE", r"\27B1", r"\25B7", r"\25B8", r"\25B9", r"\25BA", r"\25BB"]


FONT_SIZE = (31,34)
LETTER_SPACING = (1.3,1.4)
def createSlide(json_file, name=None):
    ## output : slide markdown, slide json (for pix2struct for example)
    if name is not None:
        c = Content(json_file, name)
    else:
        c = Content(json_file)

    # Create layout
    title_page = TitlePage(c.getTitle())
    pages = [Page(item) for item in c.getContents()]
    sli = Slide(pages=[title_page] + pages)

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
        sli.setBg(ImageBackground(bg))

    ## THEME
    # select random theme
    themes = ["default", "uncover", "gaia"]
    sli.setTheme(random.choice(themes))

    ## Style
    # Section related
    sli.addStyle("section {display: flex;flex-flow: column; font-size:%.3fpx; letter-spacing:%.3fpx;}" % (random.uniform(FONT_SIZE[0],FONT_SIZE[1]), random.uniform(LETTER_SPACING[0], LETTER_SPACING[1])))
    # Footer related
    sli.addStyle("header {overflow:visible}")
    sli.addStyle("header > img.logo {position:absolute; right:15px; height: 120px;}")

    # Bullet point related
    sli.addStyle("ul > li::marker {content: '%s  ';}" % random.choice(bullet_styles))
    return sli.build(), sli.build2()

sli_md, sli_json = createSlide("/home/travis/Documents/these/projects/Slide-Generator/sum_slide.json", "Photography")
with open("test.md", "w") as f:
    f.write(sli_md)
with open("test.json", "w") as f:
    f.write(json.dumps(sli_json))