from CSE8AImage import *

# Define your image_complement function here: 
def image_complement(img):
    if img == []:
        return img
    for i in range(len(img)):
        for j in range(len(img[i])):
            temp = img[i][j]
            img[i][j] = (temp[2], temp[1], temp[0])
    return img