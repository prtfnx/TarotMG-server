from PIL import Image
"""Collect of functions to operate with images"""


def square_set(list_of_path):
    """Make from 4 images one set in square form"""
    list_of_images = []
    for path in list_of_path:
        list_of_images.append(Image.open(path))
    img = list_of_images[0]  # to take size and mode
    (l, h), img_mode = img.size, img.mode  # length and height, mode of img
    image_set = Image.new(img_mode, (2*l, 2*h),)  # create imageset
    # part set in 4 parts
    list_of_boxes = [ (0, 0, l,     h),
                      (l, 0, 2*l,   h),
                      (0, h, l,   2*h),
                      (l, h, 2*l, 2*h)]
    for image, box in zip(list_of_images, list_of_boxes):
        # paste all images to imageset
        image_set.paste(image.resize((l,h)), box)
    return image_set
