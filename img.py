from PIL import Image
from numpy import array
im_1 = Image.open(r"image path")
a = array(im_1)
print(a)
