from CSE8AImage import *

def getBrightestPixel(img):
    index = -1
    z = None
    for r in range(len(img)):
        for c in range(len(img[r])):
            temp = img[r][c]
            x = 0.2126 * temp[0] + 0.7152 * temp[1] + 0.0722 * temp[2]
            if x > index:
                index = x
                z = temp
    return z

def getDarkestPixel(img):
    index = 256
    z = None
    for r in range(len(img)):
        for c in range(len(img[r])):
            temp = img[r][c]
            x = 0.2126 * temp[0] + 0.7152 * temp[1] + 0.0722 * temp[2]
            if x < index:
                index = x
                z = temp
    return z


print(getBrightestPixel([[(0, 0, 0), (100, 100, 100)], [(255, 255, 255), (50, 100, 200)]]))
print(getDarkestPixel([[(0, 0, 0), (100, 100, 100)], [(255, 255, 255), (50, 100, 200)]]))