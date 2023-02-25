# import cv2
import pytesseract

import os, glob

from PIL import Image
from pathlib import Path

os.environ['OMP_THREAD_LIMIT'] = '1'

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Set input path
inputPath = f'input\\'
outputPath = 'output\\'

imgNo = 1

# Recurse over all jpg files
for path in Path(inputPath).rglob('*.jpg'):
	
	# Get its file path, and name
	filepath, filename = os.path.split(path)
	prefix, extension = filename.split('.')
	file = path.as_posix()

	print(file)
	print('####')
	print(f'# Image: {imgNo}')

	try:

		text = pytesseract.image_to_string(file, timeout=30)

	except RuntimeError as timeout_error:

		print('# Error: RuntimeError')

	except UnicodeDecodeError as unicode_error:

		print('# Error: UnicodeDecodeError')
	
	else:

			print('# Writing file')

			try:

					with open(f'{outputPath}\\{prefix}.txt', 'w') as f:
  				
						f.write(text)

			except FileExistsError as fileexists_error:

				print('# Error: FileExistsError')

	print('####')
	print('')
	imgNo += 1
