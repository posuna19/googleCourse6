import PIL

from PIL import Image

print("Hello")

im = Image.open("img1.png")
im.rotate(45)
im.show()