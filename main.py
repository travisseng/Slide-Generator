from content import Content
from layout import Page, Slide, ImageBackground
# Get content
c = Content("/home/tseng/projects/slide_generator/output/500px/sum_slide.json")
# Create layout
pages = [Page(item) for item in c.getContents()]
sli = Slide(pages=pages)
# Customize template and style
sli.setBg(ImageBackground("/home/tseng/projects/slide_generator_clean/backgrounds/aaabstract (1).png"))
print(sli.build())