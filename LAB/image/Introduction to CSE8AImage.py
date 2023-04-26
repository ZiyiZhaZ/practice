from CSE8AImage import *

img = load_img('images/star.png')

result = img_str_to_file(img, 'star_str.txt') # TODO#2: Use img_str_to_file

print(result[0:30])

# TODO#3: Print the pixel at row 0 and column 0
print(result[0:15])