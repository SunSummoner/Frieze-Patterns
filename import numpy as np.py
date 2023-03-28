import numpy as np
import cv2 as cv 
from PIL import Image

image = Image.open('C:/Users/DELL/Desktop/Frieze_hop.png')

new_image = image.resize((400,57))
new_image.save('C:/Users/DELL/Desktop/Frieze_hop2.png')


img = cv.imread('C:/Users/DELL/Desktop/Frieze_hop2.png')
assert img is not None, "file could not be read, check with os.path.exists()"

print(img.shape)

x = 100

print(x)
c1=0
c2=0

for i in range(0,57):
    for j in range (0,x):
        a=img[i,j]
        
        b=img[i,j+x]
        c=img[i,j+2*x]
        d =img[i,j+3*x]

        #if ((a==b).all() and (a==c).all() and (c==d).all())
        if (a[1]==b[1] & a[1]==c[1] & a[1]==d[1] & a[2]==b[2] & a[2]==c[2] & a[2]==d[2] & a[0]==b[0] & a[0]==c[0] & a[0]==d[0]):
            print("ok",i,"  ",j,"  ",2*j,"  ",3*j)
            c1+=1
        else:
            print("Not matched",i,"  ",j)
            c2+=1

print(c1, "  ", c2)
