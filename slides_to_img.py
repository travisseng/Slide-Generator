import subprocess
from threading import Thread
import fitz
import glob
from PIL import Image, ImageDraw

## get marp commands
script_path = "./utils/marp_pdf.sh"
rc = subprocess.call(script_path)
print("Marp commands created")

def run_script(python_script):
    print(python_script)
    rc = subprocess.call(python_script, shell=True)
    return

def run_bash(bash_script):
    rc = subprocess.call(bash_script)
    return

rc = subprocess.run("pkill -f distributed_computing", shell=True)
a = Thread(target=run_script, args=["python /home/tseng/projects/utils/distributed_computing/start_computing_server.py -t ./commands_marp_auto.txt -p 2050"])
# subprocess.Popen("python /home/tseng/projects/utils/distributed_computing/start_computing_server.py -t ./commands_marp_auto.txt -p 2050", shell=True)
b = Thread(target=run_bash, args=["./utils/distributed_computing.sh"])

a.start()
b.start()
a.join()
b.join()
print("Finish generated marp pdf")

## parse pdf
import tqdm
import os
pdf_files = sorted(glob.glob("output/*/*.pdf"))
for pdf_file in tqdm.tqdm(pdf_files):
    pdf_nb = pdf_file.split("/")[-2]
    os.makedirs("output/%s/images/" % (pdf_nb), exist_ok=True)
    pdf = fitz.open(pdf_file)
    for page in pdf:
        pix = page.get_pixmap()
        img_path = "output/%s/images/%s.%03d.jpg" % (pdf_nb, pdf_nb, page.number)
        with Image.frombytes("RGB", [pix.width, pix.height], pix.samples) as im:
            im.save(img_path, quality=90)
        