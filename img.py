from PIL import Image
from numpy import array
im_1 = Image.open(r"C:\Users\DELL\Desktop\CIC\Semester 4\Talks\IMG-20230120-WA0012.jpg")
a = array(im_1)
print(a)