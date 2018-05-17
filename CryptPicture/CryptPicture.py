from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def crypt_color(img):
    def jiamiunit(x):
        x = str(bin(x))[2::]
        x = "0" * (8 - len(x)) + x
        x = "0b" + x[::-1]
        return int(x, 2)

    for row in img:
        for col in row:
            r = col[0]
            g = col[1]
            b = col[2]
            col[0] = jiamiunit(b)
            col[1] = jiamiunit(g)
            col[2] = jiamiunit(r)
    return img


def showimg(img, figure="Image", title="image"):
    plt.figure(figure)  # 图像窗口名称
    plt.imshow(img)
    plt.axis('on')  # 关掉坐标轴为 off
    plt.title(title)  # 图像题目
    plt.show()

def encrypt_reverse(img):
    for i in range(10):
        for i in range(len(img)):
            if i % 2 == 0:
                newarr = img[i].tolist()
                newarr.reverse()
                img[i] = np.array(newarr)
        for i in range(len(img[0])):
            if i % 2 == 0:
                newarr = img[:, i].tolist()
                newarr.reverse()
                img[:, i] = np.array(newarr)
        for i in range(len(img)):
            if i % 2 == 1:
                newarr = img[i].tolist()
                newarr.reverse()
                img[i] = np.array(newarr)
        for i in range(len(img[0])):
            if i % 2 == 1:
                newarr = img[:, i].tolist()
                newarr.reverse()
                img[:, i] = np.array(newarr)
    return img

def decrypt_revserse(img):
    for i in range(len(img[0])):
        if i % 2 == 1:
            newarr = img[:, i].tolist()
            newarr.reverse()
            img[:, i] = np.array(newarr)
    for i in range(len(img)):
        if i % 2 == 1:
            newarr = img[i].tolist()
            newarr.reverse()
            img[i] = np.array(newarr)
    for i in range(len(img[0])):
        if i % 2 == 0:
            newarr = img[:, i].tolist()
            newarr.reverse()
            img[:, i] = np.array(newarr)
    for i in range(len(img)):
        if i % 2 == 0:
            newarr = img[i].tolist()
            newarr.reverse()
            img[i] = np.array(newarr)
    return img

