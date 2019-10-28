# Imports
from PIL import Image
import numpy as np
import operator
from collections import defaultdict
from functools import reduce
import os
import sys

class pixelator:
    def __init__(self, in_path, palette, size, sensitivity_multiplier=10):
        # If the palette exceeds the max number of colors, reduce it to the first 256 colors listed.
        if len(palette) > 256:
            palette=palette[0:255]
        # Populate 256 colors for palette to sample from
        # (to match the library pillow/PIL used for image processing)
        while len(palette) < 256:
            palette.append((0, 0, 0))
        # Make the palette flat
        flat_palette = reduce(lambda a, b: a+b, palette)
        # Assert that the len of the palette is exactly 768
        assert len(flat_palette) == 768
        # Create and populate an image to hold the palette
        palette_img = Image.new('P', (1, 1), 0)
        palette_img.putpalette(flat_palette)
        # Open the input image
        input = Image.open(in_path)
        # Get the image size
        self.img_size = input.size
        # Resize the image for Sensitivity purposes, quantize the image with the palette and convert the image back to RGB for sampling
        input=input.resize((size[0] * sensitivity_multiplier, size[1] * sensitivity_multiplier), Image.BICUBIC).quantize(palette=palette_img).convert('RGB')
        # Create an output image and data object
        self.out_image = Image.new('RGB', size)
        self.out_data=np.empty([size[0],size[1],3])
        # Iterate through all pixels in the output size spec to average color over
        for x in range(size[0]):
            for y in range(size[1]):
                histogram = defaultdict(int)
                for x2 in range(x * sensitivity_multiplier, (x + 1) * sensitivity_multiplier):
                    for y2 in range(y * sensitivity_multiplier, (y + 1) * sensitivity_multiplier):
                        histogram[input.getpixel((x2,y2))] += 1
                if sys.version_info[0] == 3:
                    color = max(histogram.items(), key=operator.itemgetter(1))[0]
                elif sys.version_info[0] == 2:
                    color = max(histogram.iteritems(), key=operator.itemgetter(1))[0]
                self.out_data[x,y]=color
                self.out_image.putpixel((x, y), color)

    def resize_out_img(self, to_original=True, size=True):
        if to_original and size:
            # Resize the output image to its original dimensions
            self.out_image = self.out_image.resize(self.img_size)
        else:
            self.out_image = self.out_image.resize(size)
        return self

    def save_out_img(self, path, overwrite=False):
    # Save the output image
        if os.path.exists(path):
            if overwrite:
                os.remove(path)
                self.out_image.save(path)
            else:
                print ("Path exist but overwrite=false. Can not save image.")
        else:
            self.out_image.save(path)
