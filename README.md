## OCRMyManga

OCR My Manga is a tool to help you OCR your manga. Utilizing the Google Cloud Vision API, it can automatically detect text in your manga and output it to a text file.

OCRMyManga is written in Python. It is still in development, so there may be bugs.

<b> SINCE THIS TOOL USES THE GCLOUD LIBRARY, YOU WILL NEED TO HAVE A GOOGLE CLOUD ACCOUNT TO USE IT. THIS MAY INCUR MONETARY COSTS FOR LARGE OCR TASKS > 1000 pages</b>

## Installation

This tool REQUIRES a Google Cloud Vision API Key. Follow these instructions to get one: https://cloud.google.com/vision/docs/setup

Then, install OCRMyManga from pip with the following command:
`pip install ocrmymanga`

## Usage

OCRMyManga is a command line tool. It can be run with the following command:
It will ONLY output into pdf format.

`ocrmymanga [-h] [INPUT] [-o OUTPUT] [-b] [-c CREDS] [-v]`

-h: help
-b: batch process
-c: credential file for google vision
-v: verbose

## Permitted file types

OCRMyManga can only OCR the following file types:
.png
.jpg
.jpeg
.cbz

Support for other file types may be added in the future.

## Cookbook

### OCR a single file

`ocrmymanga input.jpg -o output.pdf`

### Batch OCR a directory

`ocrmymanga input_dir -o output_dir -b`

### OCR with a custom credential file

`ocrmymanga input.jpg -o output.pdf -c creds.json`

(-c will default to credentials.json)

### Github Link

https://github.com/D0rkKnight/OCRMyManga
