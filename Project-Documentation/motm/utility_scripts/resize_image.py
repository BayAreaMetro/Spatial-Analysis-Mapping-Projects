# Docs: https://pypi.python.org/pypi/python-resize-image

from PIL import Image
from resizeimage import resizeimage
import glob, os

#directory_path = r"/Users/jcroff/Box/MOTM_Uploads/motm_images/*.png"

def resize_and_crop(img_path, size, crop_type='top'):
    """
    Resize and crop an image to fit the specified size.

    args:
    img_path: path for the image to resize.
    size: `(width, height)` tuple.
    crop_type: can be 'top', 'middle' or 'bottom', depending on this
    value, the image will cropped getting the 'top/left', 'middle' or
    'bottom/right' of the image to fit the size.
    raises:
    Exception: if can not open the file in img_path of there is problems
    to save the image.
    ValueError: if an invalid `crop_type` is provided.
    """
    # If height is higher we resize vertically, if not we resize horizontally
    img = Image.open(img_path)
    # Get current and desired ratio for the images
    img_ratio = img.size[0] / float(img.size[1])
    ratio = size[0] / float(size[1])
    #The image is scaled/cropped vertically or horizontally depending on the ratio
    if ratio > img_ratio:
        img = img.resize((size[0], int(round(size[0] * img.size[1] / img.size[0]))),
            Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, img.size[0], size[1])
        elif crop_type == 'middle':
            box = (0, int(round((img.size[1] - size[1]) / 2)), img.size[0],
                int(round((img.size[1] + size[1]) / 2)))
        elif crop_type == 'bottom':
            box = (0, img.size[1] - size[1], img.size[0], img.size[1])
        else :
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    elif ratio < img_ratio:
        img = img.resize((int(round(size[1] * img.size[0] / img.size[1])), size[1]),
            Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, size[0], img.size[1])
        elif crop_type == 'middle':
            box = (int(round((img.size[0] - size[0]) / 2)), 0,
                int(round((img.size[0] + size[0]) / 2)), img.size[1])
        elif crop_type == 'bottom':
            box = (img.size[0] - size[0], 0, img.size[0], img.size[1])
        else :
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    else :
        img = img.resize((size[0], size[1]),
            Image.ANTIALIAS)
    # If the scale is the same, we do not need to crop
    file, ext = os.path.splitext(img_path)
    img.save(file + "_thumbnail.png", "PNG")
    #img.save(modified_path)

#provide path to directory of images
def resize_imgs_directory(size, dir_path, crop_type):
    """
    Resize and crop each image in a directory to fit a certain size 

    args:
    dir_path: path for directory of images to resize.
    size: `(width, height)` tuple.
    crop_type: can be 'top', 'middle' or 'bottom', depending on this
    value, the image will cropped getting the 'top/left', 'middle' or
    'bottom/right' of the image to fit the size. 
    """
    for img_path in glob.glob(dir_path):
        resize_and_crop(img_path, size, crop_type)

#resize_imgs_directory((600,400), directory_path, crop_type='top')

png_path = r"/Users/jcroff/Box/MOTM_Uploads/2017_12/Image Files/motm_12_18_17.png"
thumb_size = (600,400)

resize_and_crop(png_path, thumb_size, crop_type='top')



