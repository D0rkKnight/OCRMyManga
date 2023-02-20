import json
from PIL import Image, ImageDraw
from io import BytesIO
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileMerger

# Load JSON data
with open('ocr.json', 'r') as f:
    data = json.load(f)

# Load image
img = Image.open('resources/wakeupcat.jpg')

# Create in-memory PDF file
pdf_buffer = BytesIO()
can = canvas.Canvas(pdf_buffer)
draw = ImageDraw.Draw(img)

# Draw text on image and PDF
for annotation in data['text_annotations']:
    description = annotation['description']
    poly = annotation['bounding_poly']['vertices']
    coords = [(p['x'], img.size[1]-p['y']) for p in poly]
    draw.polygon(coords, outline=(255, 0, 0))
    can.drawString(coords[0][0], coords[0][1], description)

# Save PDF file
can.save()
pdf_buffer.seek(0)

# Merge PDF files
pdf_merger = PdfFileMerger()
pdf_merger.append(pdf_buffer)
pdf_merger.write('output.pdf')
pdf_merger.close()
