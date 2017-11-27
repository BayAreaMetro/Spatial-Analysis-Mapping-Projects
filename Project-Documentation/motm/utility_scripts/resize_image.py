# Docs: https://pypi.python.org/pypi/python-resize-image

from PIL import Image
from resizeimage import resizeimage

image_path = r"/Users/JoshCroff/Documents/Test_Images/motm_11_09_17_website.png"
save_file = r"/Users/JoshCroff/Documents/Test_Images/motm_11_09_17_thumbnail.png"

#fd_img = open(image_path, 'r')
#img = Image.open(fd_img)
#img = resizeimage.resize_cover(img, [600, 400])
#img.save(save_file, img.format)
#fd_img.close()

fd_img = open(image_path, 'r')
img = Image.open(fd_img)
img = resizeimage.resize_thumbnail(img, [600, 400])
img.save(save_file, img.format)
fd_img.close()