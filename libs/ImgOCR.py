import pandas as pd
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pdf2image import convert_from_path
from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)



# Function to convert to Strings
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1

#function to find all floats values from list
def solve(lis):
    for x in lis:
        try:
            float(x)
            return True
        except:
            return False

def ocr_core(filename):

    text = pytesseract.pytesseract.image_to_string(Image.open(filename))
    return text  # Then we will print the text in the image
