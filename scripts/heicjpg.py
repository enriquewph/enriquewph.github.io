#!/bin/python3

import io
import os
import pyheif
import PIL
import exifread

# Get list of HEIF and HEIC files in directory
directory = 'assets/images/'
files = []
for root, dirs, filenames in os.walk(directory):
    for filename in filenames:
        if filename.lower().endswith('.heic'):
            files.append(os.path.join(root, filename))

# Convert each file to JPEG
for filename in files:
    image = pyheif.read_heif(filename)
    for metadata in image.metadata or []:
        if metadata['type'] == 'Exif':
            fstream = io.BytesIO(metadata['data'][6:])
            # now just convert to jpeg
    pi = PIL.Image.open(fstream)
    pi.save(os.path.splitext(filename)[0] + '.jpg', "JPEG")
