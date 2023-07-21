import os

from PIL import Image

for f in os.listdir("./pngs"):
    if f.endswith(".png"):
        im = Image.open(f"./pngs/{f}")
        im = im.crop(im.convert("RGBa").getbbox())
        im.save(f"./pngs-cropped/{f}")
