from fpdf import FPDF
import os
from PIL import Image

def convert_to_pdf(path,dest,name):
    final=[]
    images = sorted(os.listdir(path))
    for i in images[1:]:
        img = Image.open(f"{path}/{i}")
        imgc = img.convert('RGB')
        final.append(imgc)
    img0=Image.open(f"{path}/{images[0]}")
    imgc0=img0.convert("RGB")
    imgc0.save(f"{dest}/{name}.pdf",save_all=True,append_images=final)



convert_to_pdf("test_photos/test6","test_pdf","test6")