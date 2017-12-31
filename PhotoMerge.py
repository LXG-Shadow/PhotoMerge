#-*- coding:utf-8 -*-
from PIL import Image,ImageDraw
import os

'''
#here is tested data, ignore them
picroute = "/Users/luyijou/Desktop/ Mine/图片/表情包/csgo表情"
size = (394,248)
width,height = size
heightnum = 13
widthnum = 13
picnum = 158
pictotalnum = heightnum*widthnum
'''

def photomerge(imgs=[],imgnum=0,widthimg=0,heightimg=0,size=(0,0)):
    width, height = size
    pictotalnum = heightimg * widthimg
    img = Image.new("RGB", (width * widthimg, height * heightimg), (255, 255, 255))
    for i in range(0, pictotalnum, 1):
        hnum = (i // widthimg) * height
        wnum = (i % widthimg) * width
        if i + 1 > imgnum:
            pstdimg = imgs[0].resize(size)
        else:
            pstdimg = imgs[i+1].resize(size)
        img.paste(pstdimg, (wnum, hnum))
    return img


def openimg(imgroute):
    try:
        imgs = [Image.open(os.path.join(picroute,"replace.jpg"))]
    except:
        image = Image.new("RGB", (100, 100), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=(255,255,255))
        image.save(os.path.join(picroute,"replace.jpg"), "jpeg")


    imgs = [Image.open(os.path.join(imgroute,f)) for f in os.listdir(imgroute)
            if os.path.isfile(os.path.join(imgroute,f)) and os.path.splitext(f)[0] != "replace"
            and (os.path.splitext(f)[1] == ".jpg" or os.path.splitext(f)[1] == ".png")]
    imgs.insert(0,Image.open(os.path.join(picroute,"replace.jpg")))
    return imgs

if __name__ == "__main__" :
    picroute = input("Enter the Pictures folder Route: ")
    width, height = map(lambda x: int(x), input("Enter Each Pictures size(width height): ").split(sep=" "))
    size = (width, height)
    widthnum,heightnum, = map(lambda x: int(x), input("Enter how many picture in a line and a row: ").split(sep=" "))
    imgs = openimg(picroute)
    photomerge(imgs,len(imgs)-1,widthnum,heightnum,size).save(os.path.join(picroute,"Merged.jpg"),"jpeg")


