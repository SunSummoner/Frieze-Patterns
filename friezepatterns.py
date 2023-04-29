import cv2
import numpy as np
from PIL import Image


# Load the image
img = cv2.imread("C:\\Users\\anant\\Desktop\\Patterns\\Images\\40.png")
img1= Image.open("C:\\Users\\anant\\Desktop\\Patterns\\Images\\40.png")

#1. Hop
def hop_frieze_pattern(image):
    pattern_size = 5
    frieze1 = np.concatenate([image]*pattern_size, axis=1)
    cv2.imwrite("C:\\Users\\anant\\Desktop\\Patterns\\Hop\\40.jpg", frieze1)

#2. Sidle
def create_sidle_frieze_pattern(image):
    width, height = image.size
    frieze_pattern = Image.new("RGB", (width * 2, height))
    frieze_pattern.paste(image, (0, 0))
    frieze_pattern.paste(image.transpose(Image.FLIP_LEFT_RIGHT), (width, 0))
    pattern_size = 5
    frieze2 = np.concatenate([frieze_pattern]*pattern_size, axis=1)
    cv2.imwrite("C:\\Users\\anant\\Desktop\\Patterns\\Sidle\\40.jpg", frieze2)

#3. Glide Pattern
def create_glide_frieze_pattern(image):
    width, height = image.size
    frieze_pattern = Image.new("RGB", (width * 2, height))
    frieze_pattern.paste(image, (0, 0))
    frieze_pattern.paste(image.transpose(Image.FLIP_TOP_BOTTOM), (width, 0))
    pattern_size = 5
    frieze3 = np.concatenate([frieze_pattern]*pattern_size, axis=1)
    cv2.imwrite("C:\\Users\\anant\\Desktop\\Patterns\\Glide\\40.jpg", frieze3)

#4. Spinning Hop
def create_spinning_hop_frieze_pattern(image):
    n=5
    zero = np.zeros_like(image)
    img1 = cv2.vconcat([ image,  cv2.rotate(image,cv2.ROTATE_180)])
    img22 = cv2.vconcat([zero, cv2.flip(image, 0)])
    img2 = cv2.vconcat([image,  cv2.rotate(image,cv2.ROTATE_180)])
    img3 = cv2.hconcat([img1, img2])
    for i in range(n):
        frieze4 = cv2.hconcat([img3, img3])
    if i>0:
        frieze4 = cv2.hconcat([frieze4, img3])
    cv2.imwrite("C:\\Users\\anant\\Desktop\\Patterns\\SpinningHop\\40.jpg", frieze4)

#5 Jump
def create_jump_frieze_pattern(image):
    n = 5
    zero = np.zeros_like(image)
    img1 = cv2.vconcat([ image,  cv2.flip(image,0)])
    img2 = cv2.vconcat([image,  cv2.flip(image,0)])
    img3 = cv2.hconcat([img1, img2])
    for i in range(n):
     frieze5 = cv2.hconcat([img3, img3])
    if i>0:
        frieze5 = cv2.hconcat([frieze5, img3])
    cv2.imwrite("C:\\Users\\anant\\Desktop\\Patterns\\Jump\\40.jpg", frieze5)

#6. Spinning Jump
def create_spinning_jump_frieze_pattern(image):
    n = 5
    zero = np.zeros_like(image)
    img1 = cv2.vconcat([image, cv2.flip(image,0)])
    img3 = cv2.hconcat([img1, cv2.rotate(img1,cv2.ROTATE_180)])
    for i in range(n):
        frieze6 = cv2.hconcat([img3, img3])
    if i>0:
        frieze6 = cv2.hconcat([frieze6, img3])
    cv2.imwrite('C:\\Users\\anant\\Desktop\\Patterns\\SpinningJump\\40.jpg', frieze6)

#2. SpinningSidle
def create_spinning_sidle_frieze_pattern(image):
    image = np.array(cv2.resize(image, (800, 800)))
    n = 5
    zero = np.zeros_like(image)
    img1 = cv2.hconcat([image, cv2.flip(image,cv2.ROTATE_180)])
    img2 = cv2.hconcat([cv2.flip(img1,cv2.ROTATE_90_CLOCKWISE)])
    img3 = cv2.hconcat([img1, img2])
    for i in range(n):
     frieze7 = cv2.hconcat([img3, img3])
    if i>0:
        frieze7 = cv2.hconcat([frieze7, img3])
    cv2.imwrite("C:\\Users\\anant\\Desktop\\Patterns\\SpinningSidle\\40.jpg", frieze7)

frieze1 = hop_frieze_pattern(img)
frieze2 = create_sidle_frieze_pattern(img1)
frieze3 = create_glide_frieze_pattern(img1)
frieze4 = create_spinning_hop_frieze_pattern(img)
frieze5 = create_jump_frieze_pattern(img)
frieze6 = create_spinning_jump_frieze_pattern(img)
frieze7 = create_spinning_sidle_frieze_pattern(img)





