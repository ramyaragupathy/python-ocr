# Python Imaging Library & pytesseract
from PIL import Image
import pytesseract

# open the relevant image file
im = Image.open('book.jpg')
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR"'
text_pytesseract=pytesseract.image_to_string(im, config=tessdata_dir_config)

# output the text present in the image
print(text_pytesseractt)
