Pixelator
==========
A simple python package to pixelate images given a color palette

Features
--------

- Users can:
  1. Load in array data, image files or capture directly from a camera
  2. Pixelate images to a specific color palette and image resolution
  3. Access pixelated array data or write it back to an image file

Technical Docs
--------
https://connor-makowski.github.io/pixelator/pixelator.html

Setup
----------

Make sure you have Python 3.6.x (or higher). You can download it [here](https://www.python.org/downloads/).

### Installation

```
pip install pixelator
```

### Getting Started
Import the pixelator into your project
```
from pixelator import Pixelator
```

Some important notes:
- All data is stored and processed as BGR (to match open cv2)
  - EG: Provided pallettes should be in BGR

### Examples

Load from a file:
```
from pixelator import Pixelator
# Use the input filename provided
image = Pixelator(filename='./images/input.jpg')
# Pixelate the image to a 28x28 black and white array
pixelated_image = image.pixelate(
    width=28,
    height=28,
    palette=[[0,0,0],[255,255,255]]
)
# Write to `output.png` scaled up to a 500x500 image (to be easily viewed)
pixelated_image.write(filename='./images/output_test_1.jpg', width=300, height=300)
```
Input:
![](images/input.jpg)

Output:
![](images/output_test_1.jpg)

Capture from a webcam:
```
from pixelator import Pixelator
# Capture from a webcam since no data or filename is provided
image = Pixelator()

# Pixelate the image to a 64x64 black, white and multiple gray array
pixelated_image = image.pixelate(
    width=64,
    height=64,
    palette=[[0,0,0],[80,80,80],[160,160,160],[200,200,200],[255,255,255]]
)
# Write to `output.png` scaled up to a 500x500 image (to be easily viewed)
pixelated_image.write(filename='./images/output_test_3.jpg', width=300, height=300)
```
![](images/output_test_3.jpg)

Access Pixelator Data:
```
from pixelator import Pixelator
# Use the input filename provided
image = Pixelator(filename='./images/input.jpg')
# Pixelate the image to a 28x28 black and white array
pixelated_image = image.pixelate(
    width=28,
    height=28,
    palette=[[0,0,0],[255,255,255]]
)
# Show pixelated image data
print(pixelated_image.data)
```
