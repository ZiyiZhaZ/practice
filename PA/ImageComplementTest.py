from CSE8AImage import *
from ImageComplement import *

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

def test_complement_1():
    cat = load_img("images/cat.jpg")
    img = image_complement(cat)
    save_img(img, "images/complement_cat.jpg")

# add test_complement_2 here:

test_complement_1()
# test_complement_2()
def test_complement_2():
    img = create_img(200, 200, (255, 255, 0))
    img = image_complement(img)
    save_img(img, "images/complement_img.jpg")

test_complement_2()