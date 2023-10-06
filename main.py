from controller import createSlide
import glob
import os
import json
import tqdm
import random
import utils
os.makedirs("output", exist_ok=True)

random.seed(0)
json_files = sorted(glob.glob("../slide_generator/output/*/sum_slide.json"))
for json_file in tqdm.tqdm(json_files):
    # print(json_file)
    name_sli = json_file.split("/")[-2]
    sli_md, sli_json = createSlide(json_file)
    os.makedirs("output/{}".format(name_sli), exist_ok=True)

    with open("output/{}/slide.md".format(name_sli), "w") as file:
        file.write(sli_md)
    with open("output/{}/slide.json".format(name_sli), "w") as file:
        file.write(json.dumps(sli_json))
    with open("output/{}/slide_md.json".format(name_sli), "w") as file:
        # print(sli_json)
        file.write(json.dumps([utils.dict2markdown(sli_j) for sli_j in sli_json]))