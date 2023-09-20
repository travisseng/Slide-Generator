import glob
import os
import random

random.seed(0)
label_files = glob.glob("output/*/labels/*.txt")
print("%d files found." % len(label_files))
contains_images_label = []
contains_images_img = []
val_contains_images_label = []
val_contains_images_img = []
i=0
os.makedirs("annotations", exist_ok=True)
root_dir = "/home/tseng/projects/slide_generator_clean/"
for label in label_files:
    with open(label, 'r') as f:
        line = f.read(1)
        if line == "" or line[0] not in {"1", "0"}:
            # print(line)
            # i = i+1
            # print(i)
            continue

        else:
            
            # there is a annotation
            if random.random() > 0.9:
                val_contains_images_label.append(root_dir + label + "\n")
                val_contains_images_img.append(root_dir + label.replace("labels", "images").replace("txt", "jpg") + '\n')
            else:
                contains_images_label.append(root_dir + label + "\n")
                contains_images_img.append(root_dir + label.replace("labels", "images").replace("txt", "jpg") + '\n')
with open("annotations/img_labels.txt", "w") as f:
    f.writelines(contains_images_label)
with open("annotations/img_img.txt", "w") as f:
    f.writelines(contains_images_img)
with open("annotations/img_val_labels.txt", "w") as f:
    f.writelines(val_contains_images_label)
with open("annotations/img_val_img.txt", "w") as f:
    f.writelines(val_contains_images_img)