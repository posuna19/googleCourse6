#!/usr/bin/env python

import glob
from PIL import Image

srcDir = ".\\imgs\\images\\*"
desDir = ".\\imgs\\opt\\icons\\"

white = (255, 255, 255)
black = (0, 0, 0)
bg_color = white

for imgName in glob.glob(srcDir):
    #print(imgName)
    nameOnly = imgName[14:]
    #print(nameOnly)

    filePath = desDir + nameOnly + ".jpeg"
    print(filePath)

    if nameOnly.find("white") >= 0:
        bg_color = black
    else:
        bg_color = white

    img = Image.open(imgName).convert("RGBA")
    out = Image.new("RGBA",(192, 192), bg_color)
    out.paste(img, img)
    out = out.convert("RGB").rotate(-90).resize((128, 128))
    out.save(filePath)

print("End!")

