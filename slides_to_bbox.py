## parse pdf
import tqdm
import glob
import fitz
import os
import orjson
def to_yolo_format(x1,y1,x2,y2,img_w, img_h, cls=None):
    x_c = (x1+x2)/2
    y_c = (y1+y2)/2
    w = x2-x1
    h = y2-y1
    if cls is None:
        return (x_c/img_w,y_c/img_h, w/img_w, h/img_h)
    else:
        return (cls, x_c/img_w,y_c/img_h, w/img_w, h/img_h)
pdf_files = sorted(glob.glob("output/*/*.pdf"))

annotate_words = False
annotate_graphics = True
import time
annotations_2 = {}
for pdf_file in tqdm.tqdm(pdf_files):
    pdf_nb = pdf_file.split("/")[-2]
    pdf = fitz.open(pdf_file)
    
    os.makedirs("output/%s/labels/" % (pdf_nb), exist_ok=True)
    
    for page in pdf:
        ## save img
        
        # pix = page.get_pixmap()
        
        img_path = "output/%s/images/%s.%03d.jpg" % (pdf_nb, pdf_nb, page.number)
        # print(img_path)
        # pix.save(img_path)

        ## get words
        # words = page.get_text("words")
        ## get images
        
        img_list = page.get_images(full=True)
        
        ## get drawings 
        # drawings = page.get_drawings()
        annotations = []
        # tabs = page.find_tables()  # detect the tables
        # if annotate_words:
        #     for word in words:
        #         bbox_yolo = to_yolo_format(word[0], word[1], word[2], word[3],pix.width, pix.height)
        #         annotations.append("%d %f %f %f %f\n" % (bbox_yolo[0], bbox_yolo[1], bbox_yolo[2], bbox_yolo[3], bbox_yolo[4]))
        if annotate_graphics:
            for img_el in img_list:
                rect = page.get_image_bbox(img_el)
                
                bbox_yolo = to_yolo_format(rect[0],rect[1], rect[2], rect[3], 960, 540, 0)
                
                if bbox_yolo[3] > 0.75:
                    continue #this is background image
                annotations.append("%d %f %f %f %f\n" % (bbox_yolo[0], bbox_yolo[1], bbox_yolo[2], bbox_yolo[3], bbox_yolo[4]))
                # draw.rectangle((rect[0],rect[1], rect[2], rect[3]), outline=(0,0,255), width=1)
            # for item in drawings:
            #     rect = item["rect"]
            #     area = (rect[2]-rect[0])*(rect[3]-rect[1])
            #     bbox_yolo = to_yolo_format(rect[0],rect[1], rect[2], rect[3], pix.width, pix.height, 0)
            #     annotations.append("%d %f %f %f %f\n" % (bbox_yolo[0], bbox_yolo[1], bbox_yolo[2], bbox_yolo[3], bbox_yolo[4]))
                # print(area)
            # for i,tab in enumerate(tabs):
            #     print("find tab in " + img_path, tab.bbox)
            #     rect = tab.bbox
            #     bbox_yolo = to_yolo_format(rect[0],rect[1], rect[2], rect[3], pix.width, pix.height, 1)
            #     annotations.append("%d %f %f %f %f\n" % (bbox_yolo[0], bbox_yolo[1], bbox_yolo[2], bbox_yolo[3], bbox_yolo[4]))
            #     if area < 518400*0.9:
            #         draw.rectangle((rect[0],rect[1], rect[2], rect[3]), outline=(0,255,0), width=1)
            # im.save(img_path, quality=90)
        with open("output/%s/labels/%s.%03d.txt" % (pdf_nb, pdf_nb, page.number), "w") as f:
            f.writelines(annotations)
        
        annotations_2[rf"%s.%03d" % (pdf_nb, page.number)] = annotations
        # print(annotations_2)
with open("output/labels.json", "wb") as f:
    f.write(orjson.dumps(annotations_2, option=orjson.OPT_INDENT_2))


        