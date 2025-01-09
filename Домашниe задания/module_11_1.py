from PIL import Image, ImageOps
from PIL import ImageEnhance as ie

im = Image.open("1735494059100.jpg")
print(im.format, im.size, im.mode)
# im.show()

rot_im = im.rotate(45) # разворачивает картинку на заданный градус
rot_im.show()

def merge(im1: Image.Image, im2:Image.Image):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new('RGB', (w, h))
    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))
    return im          # стыковка двух картинок
merge(im, im).show()

pch = ie.Contrast(im) # изменят контраст картинки
pch.enhance(7).show()

size = (500, 200)
ImageOps.contain(im, size)
im.thumbnail(size) # изменяет разрешение картинки
im.show()