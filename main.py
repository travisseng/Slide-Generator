from content import Content
from layout import Page, TitlePage, Slide, ImageBackground, ColoredBackground
import json
import random
import glob
import cv2
import numpy as np
import distinctipy


# Get content
c = Content("sum_slide.json", "Photography")

# Create layout
title_page = TitlePage(c.getTitle())
pages = [Page(item) for item in c.getContents()]
sli = Slide(pages=[title_page] + pages)

# Customize template and style
## Paginate
if random.random() > 0.2:
    sli.setPaginate(True)
else:
    sli.setPaginate(False)

## BACKGROUND
bg_prob = random.random()
if bg_prob > 0.5:
    # Get white background
    sli.setBg(ColoredBackground("white"))
elif bg_prob > 0.4:
    # Get colored background
    sli.setBg(ColoredBackground(distinctipy.get_hex(distinctipy.get_colors(1, pastel_factor=1)[0])))
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
sli.addStyle("section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}")
# Footer related
sli.addStyle("header {overflow:visible} header > img.logo {position:absolute; right:15px;}")
sli.addStyle("header > img.logo {position:absolute; right:15px;}")

## Build

with open("test.md", "w") as file:
    file.write(sli.build())
a = json.dumps(sli.build2())
print(a)