from CSE8AImage import *

def blue_filter(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            temp = img[i][j]
            img[i][j] = (0, 0, temp[2])
    return img