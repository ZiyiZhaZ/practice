from CSE8AImage import *
from Blue_Filter import *

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

def test_blue_filter_1():
    # loads cat image
    cat = load_img("images/cat.jpg")
    # applies blue filter
    img = blue_filter(cat)
    # saves image with filter
    save_img(img, "images/blue_cat.jpg")

def test_blue_filter_2():
    hopper = load_img('images/hopper.jpg')
    img = blue_filter(hopper)
    save_img(img, 'images/blue_hopper.jpg')

test_blue_filter_1() 
test_blue_filter_2()