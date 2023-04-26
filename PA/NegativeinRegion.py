import sys
sys.dont_write_bytecode = True
from CSE8AImage import *

# Define negative_region here:
def negative_region(img, top_left, w, h):
    endr = top_left[0] + h
    endc = top_left[1] + w
    if endr > height(img):
        endr = height(img)
    if endc > width(img):
        endc = width(img)
    for r in range(top_left[0], endr):
        for c in range(top_left[1], endc):
            temp = img[r][c]
            img[r][c] = (255 - temp[0], 255 - temp[1], 255 - temp[2])
    return img