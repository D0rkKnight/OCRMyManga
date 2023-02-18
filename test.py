from PyPDF2 import PdfMerger
from reportlab.pdfgen import canvas
from io import BytesIO
from PIL import Image, ImageDraw
import io
import os
import json
import pickle

# Imports the Google Cloud client library
from google.cloud import vision

# Set credentials env variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('resources/wakeupcat.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Perform text ocr on the image file
results = client.text_detection(image=image)
annotations = results.text_annotations

# Write annotations to file
file = open('ocr.json', 'w', encoding='utf-8')
file.write(str(annotations))

# Load image
img = Image.open('resources/wakeupcat.jpg')

# Create in-memory PDF file
pdf_buffer = BytesIO()
can = canvas.Canvas(pdf_buffer)
draw = ImageDraw.Draw(img)

# Draw text on image and PDF
# for annotation in annotations:
#     description = annotation.description
#     poly = annotation.bounding_poly.vertices
#     coords = [(p.x, img.size[1]-p.y) for p in poly]
#     draw.polygon(coords, outline=(255, 0, 0))
#     can.drawString(coords[0][0], coords[0][1], description)

# Save PDF file
can.save()
pdf_buffer.seek(0)

# Merge PDF files
pdf_merger = PdfMerger()
pdf_merger.append(pdf_buffer)
pdf_merger.write('output.pdf')
pdf_merger.close()
