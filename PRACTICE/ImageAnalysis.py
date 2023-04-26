from CSE8AImage import *

def getAverageGreenPixelValue(img):
    if img == [[]]:
        return float(0)
    x = 0
    y = 0
    for r in range(len(img)):
        for c in range(len(img[r])):
            x += 1
            temp = img[r][c]
            if temp[0] == 0 and temp[2] == 0:
                y += temp[1]
    return float(y/x)

def getRedTintedValues(img):
    x = 0
    for r in range(len(img)):
        for c in range(len(img[r])):
            temp = img[r][c]
            if temp[0] > temp[1] and temp[0] > temp[2]:
                x += 1
    return int(x)



img1 = [[(0, 20, 0), (0, 20, 0), (0, 100, 0), (0, 100, 0)], 
       [(0, 80, 0), (0, 80, 0), (0, 160, 0), (0, 160, 0)]] 
print(getAverageGreenPixelValue(img1))

img2 = [[]] 
print(getAverageGreenPixelValue(img2))

img3 = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], 
       [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 160, 0)]] 
print(getAverageGreenPixelValue(img3))

img4 = [[(100, 100, 100), (0, 0, 0), (100, 20, 50)], 
       [(200, 0, 0), (255, 255, 255), (10, 0, 0)]] 
print(getRedTintedValues(img4))

img5 = [[]] 
print(getRedTintedValues(img5))

img6 = [[(20, 20, 0), (40, 0, 40)], 
       [(0, 0, 0), (80, 0, 80)]] 
print(getRedTintedValues(img6))