import sys
sys.dont_write_bytecode = True
from CSE8AImage import *
from NegativeinRegion import *

"""
RGB codes for common colors. You can add on to this
if you want to experiment with different colors.
"""
black   = (0,0,0)
white   = (255,255,255)
red     = (255,0,0)
green   = (0,255,0)
blue    = (0,0,255)
yellow  = (255,255,0)
magenta = (255,0,255)
gray    = (128,128,128)
purple  = (128,0,128)

def test_negative_1():
    cat = load_img("images/cat.jpg")
    img = negative_region(cat, (110,100), 300, 250)
    save_img(img, "images/negative_cat.jpg")

def test_negative_2():
    hopper = load_img('images/hopper.jpg')
    img = negative_region(hopper, (100,100), 300, 500)
    save_img(img, 'images/negative_hopper.jpg')

test_negative_1()
test_negative_2()