# -*- coding: utf-8 -*-

from PIL import Image

import pytesseract

if __name__ == '__main__':
    img = Image.open('./en.png')
    result = pytesseract.image_to_data(img)
    print(result)