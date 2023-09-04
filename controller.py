from content import Content
from layout import Page, TitlePage, Slide, ImageBackground, ColoredBackground, GradientBackground, ImagePage, Header, Title, Text, Image, Footer
import json
import random
import glob
import cv2
import numpy as np
import distinctipy
import randomcolor
import pandas as pd
from faker import Faker
fake = Faker()

rand_color = randomcolor.RandomColor()
bullet_styles = [r"\2022", r"\2299", r"\229A", r"\229B", r"\25C9", r"\29BF", r"\29BE", r"\25C6", r"\25C7", r"\25C8", r"\2731", r"\2724", r"\2732", r"\2726", r"\2727", r"\25A0", r"\2612", r"\25A1", r"\2713", r"\2714", r"\27A2", r"\27A3", r"\27A4", r"\27AE", r"\27B1", r"\25B7", r"\25B8", r"\25B9", r"\25BA", r"\25BB", r"\25FE"]

MAX_FOOTER_CONTENT = 3
FONT_SIZE = (29,35)
LETTER_SPACING = (1.3,1.4)
LINE_HEIGHT = (1.1,1.4)
PROB_DISPLAY_TITLE = 0.8
PROB_HEADER = 0.4
PROB_FOOTER = 0.4
PADDING_HEADER_RANGE = (80,105)
PADDING_BOTTOM_RANGE = (23,40)
LOGOS_FILES = glob.glob("Logos/*.png") + glob.glob("Logos/*.jpg") + glob.glob("Logos/*.gif")
border_styles = ["dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
df = pd.read_csv("utils/world-universities.csv")
universities_data = df.to_dict(orient="list")
with open("utils/male.txt", "r") as f:
    male_names = f.read().splitlines() 
with open("utils/female.txt", "r") as f:
    female_names = f.read().splitlines() 
names = male_names + female_names
def generateRandomDate():
    random_day_nb = random.randint(1,31)
    random_year = random.randint(1990, 2099)
    random_day_name = random.choice(days)
    random_month = random.choice(months)
    return "%s %d %s %d" % (random_day_name, random_day_nb, random_month, random_year)
def generateName():
    name = random.sample(names, 2)
    return " ".join(name)
# def generateFooterContent(text_list=[], filter_content=-1, proba=0.5):
#     uni_name = random.choice(universities_data["names"])
#     uni_url = random.choice(universities_data["url"])
#     date = generateRandomDate()
#     name = generateName()
#     contents_before_filtered = text_list + [uni_name, name, uni_url, date]
#     contents = contents_before_filtered[:filter_content]
#     random.shuffle(contents)
#     return [Text(item) for item in contents if random.random() < proba]

def generateFooterContent(text_list=[], filter_content=-1, proba=0.5):
    date = generateRandomDate()
    uni_name = random.choice(universities_data["names"])
    name = fake.name()
    company = fake.company()
    url = fake.url()
    email = fake.ascii_email()
    catch_phrase = fake.catch_phrase()
    contents_before_filtered = text_list + [uni_name, name, url, email, catch_phrase, company, date]
    contents = contents_before_filtered[:filter_content]
    random.shuffle(contents)
    output = [Text(item) for item in contents if random.random() < proba]
    return output[:MAX_FOOTER_CONTENT]

def getRandomBackground(color,to="bottom"):
    if random.random() > 0.5:
        return "background-image: linear-gradient(to %s,#FFF, %s)" % (to, color)
    else:
        return "background-color: %s" % color


def generateHeaderStyle(prob_bg=0.5,prob_border=0.5):
    style_choice = ""
    margin = 0
    if random.random() < prob_bg:
        style_choice += "{};color: #000;" .format(getRandomBackground(rand_color.generate(luminosity= 'light')[0]))
    else:
        margin = random.randrange(0,15)
        style_choice += "border-bottom-style: {}; border-width: {}px; border-color:{};".format(random.choice(border_styles), random.randrange(4,8), rand_color.generate(luminosity= 'light')[0])
    padding_top = random.randrange(PADDING_HEADER_RANGE[0],PADDING_HEADER_RANGE[1])
    style = "left: {}%; right: {}%;top: 0;  box-sizing: border-box;font-size: 66%; height: {}px;line-height: 50px;padding: 10px 25px;position: absolute;font-size: 1em;font-weight: 700; display:flex; {}".format(margin, margin, padding_top,style_choice)

    # style = ""
    return style, padding_top

def generateFooterStyle(prob_bg=0.33,prob_border=0.33):
    style_choice = ""
    margin = 0
    prob = random.random()
    padding_bottom = random.randrange(PADDING_BOTTOM_RANGE[0],PADDING_BOTTOM_RANGE[1])
    if prob < prob_bg:
        style_choice += "{};color: #000;" .format(getRandomBackground(rand_color.generate(luminosity= 'light')[0], "top"))
    elif prob < prob_bg + prob_border:
        margin = random.randrange(0,15)
        top_or_btm = "top" if random.random() > 0.5 else "bottom"
        style_choice += "border-{}-style: {}; border-width: {}px; border-color:{};".format(top_or_btm,random.choice(border_styles), random.randrange(4,8), rand_color.generate(luminosity= 'light')[0])
    else:
        return "left: {}%; right: {}%;bottom: 0; box-sizing:border-box; height: {}px;line-height: 0px;display:flex;font-size:0.6em;".format(margin, margin, padding_bottom), padding_bottom
    
    style = "left: {}%; right: {}%;bottom: 0;  box-sizing: border-box; height: {}px;line-height: 0px;position: absolute;font-size: 0.6em;font-weight: 700; display:flex; {}".format(margin, margin, padding_bottom,style_choice)

    # style = ""
    return style, padding_bottom

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
    padding_bottom = None
    if hasHeader:
        styleHeader, padding_top = generateHeaderStyle()
        for i, p in enumerate(pages):
            if random.random() < 0.3:
                p.setDisplayTitle(False)
                header_content = [Title(titles[i])] + generateFooterContent([c.getTitle()], filter_content=3, proba=0.2)
                if random.random() > 0.5:
                    header_content.append(Image("../../" + random.choice(LOGOS_FILES), classe="logo",is_header=True))
                    random.shuffle(header_content)
                p.setHeader(Header(header_content))
            else:
                header_content = generateFooterContent([c.getTitle()], filter_content=3, proba=0.2)
                p.setHeader(Header(header_content))
    list_pages = [title_page] + pages
    # add random image slide for diversity
    random_image = c.getRandomImage()
    if random_image is not None:

        list_pages += [ImagePage(c.getRandomImage(), is_bg=False, title=None if random.random() > 0.5 else c.getRandomTitle()) for i in range(2)]


    # add footer
    styleFooter, padding_bottom = generateFooterStyle()
    if random.random() < PROB_HEADER:
        for p in list_pages:
            p.setFooter(Footer(generateFooterContent([c.getTitle()])))
    else:
        padding_bottom = 0
    
            
    
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
        # sli.setBg(ColoredBackground("white"))
        pass
    elif bg_prob > 0.5:
        # Get colored background
        sli.setBg(ColoredBackground(distinctipy.get_hex(distinctipy.get_colors(1, pastel_factor=1)[0])))
    elif bg_prob > 0.4:
        # Get gradient background
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
    themes = ["default", "uncover", "gaia", "dracula", "border", "graph_paper", "academic", "gradient", "rose-pine", "rose-pine-dawn"]
    sli.setTheme(random.choice(themes))

    # theme related
    if random.random() > 0.5:
        sli.addStyle(":root {--border-color: #ffffff;}")

    # Header related
    header_style = ""
    header_related = ""
    
    if hasHeader:
        header_style = styleHeader
        header_related = "padding-top: %dpx;" % (padding_top + 10)
    sli.addStyle("header {overflow:visible; color: inherit; %s}" % header_style)
    # sli.addStyle("header > div.logo {position:absolute; top: 0px; right:15px; height: 75px;}")
    sli.addStyle("header > * {margin: auto;}")
    sli.addStyle("header > p {font-size:0.6em !important;} ")

    # Footer related
    # sli.addStyle("footer {left:0; right:0; bottom:0; display:flex;font-size:0.5em;background-color:%s}" % rand_color.generate(luminosity= 'light')[0])
    sli.addStyle("footer {%s}" % styleFooter)
    sli.addStyle("footer > * {margin: auto;}")

    ## Style
    # Section related
    footer_related = "padding-bottom:%dpx" % (padding_bottom + 10)
    sli.addStyle("section {display: flex;flex-flow: column; font-size:%.3fpx; letter-spacing:%.3fpx; line-height: %.3f; %s; %s;}" % (random.uniform(FONT_SIZE[0],FONT_SIZE[1]), random.uniform(LETTER_SPACING[0], LETTER_SPACING[1]), random.uniform(LINE_HEIGHT[0], LINE_HEIGHT[1]), header_related, footer_related))


    # Bullet point related
    sli.addStyle("ul > li::marker {content: '%s  ';}" % random.choice(bullet_styles))
    return sli.build(), sli.build2()

if __name__ == "__main__":
    sli_md, sli_json = createSlide("/home/travis/Documents/these/projects/Slide-Generator/sum_slide.json", "Photography")
    with open("test.md", "w") as f:
        f.write(sli_md)
    with open("test.json", "w") as f:
        f.write(json.dumps(sli_json))
