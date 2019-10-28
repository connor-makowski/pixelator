Pixelator
==========
A simple python package to pixelate images given a color palette

Code forked and updated from an answer by user `rr-` on [StackOverflow].

Features
--------

- Users can:
  - Provide and input image
  - Specify a color palette
  - Get pixelated data returned
  - Get a pixelated image returned

Setup
----------

Make sure you have Python 3.6.x (or higher) or Python2.7.x (or higher) installed on your system. You can download it [here](https://www.python.org/downloads/).

### Installation

```
pip install pixelator
```

### Getting Started
1) Import pixelator into your project
```
from pixelator import pixelator
```

2) Set the `in_path` of the image you want to read in:
  - Example:
    ```
    in_path='path/to/image.jpg'
    ```

3) Set an RGB color `palette` to use:
  - Determines palette of colors that can be used in pixelated output
  - This is a list of RGB tuples
  - Example:
    ```
    palette = [
        (45,  50,  50),  #black
        (240, 68,  64),  #red
        (211, 223, 223), #white
        (160, 161, 67),  #green
        (233, 129, 76),  #orange
    ]
    ```

4) Choose a pixel output `size`:
  - Determines the output pixel width and height
  - This is a tuple in the form of (width, height)
  - Example:
    ```
    size=(20,20)
    ```

5) Optional - Set a `sensitivity_multiplier`:
  - This is used to sample colors from the input picture
    - Breaks each pixel into a set of sub pixels
    - The sensitivity multiplier determines the number of pixels to break the pixel into for width and height
    - A `sensitivity_multiplier` value of 10 would sample 100 (or 10*10) sub pixels from the image
  - Example:
    ```
    sensitivity_multiplier=10
    ```

6) Pixelate your image:
  ```py
  output=pixelator(
      in_path=in_path,
      palette=palette,
      size=size,
      sensitivity_multiplier=sensitivity_multiplier # This is optional
      )
  ```

### Output Data
- Raw array data is stored as a numpy object.
  - It can be called with:
    ```
    output.out_data
    ```

- Image Data is stored as a pillow object.
  - It can be called with:
    ```
    output.out_image
    ```
  - It can be saved:
    - `Path` specifies system path to save image to
    - `overwrite` specifies weather or not to overwrite a file if it exists
    ```
    output.save_out_img(path='path/to/output.jpg', overwrite=True)
    ```
  - It can be resized (this overwrites the `output.out_image`):
    - `to_original` - (Boolean) (defaults to true) takes the pixelated image and stretches it to the original photo width and height
    - `size` - (tuple`(length, width)`) (defaults to original picture size) stretches the pixelated image to any specified width and height

### Full Example
```py
from pixelator import pixelator
palette = [
    (45,  50,  50),  #black
    (240, 68,  64),  #red
    (211, 223, 223), #white
    (160, 161, 67),  #green
    (233, 129, 76),  #orange
]

sensitivity_multiplier = 10

size = (30,30)

y=pixelator(
    in_path='../images/input.jpg',
    palette=palette,
    size=size,
    sensitivity_multiplier=sensitivity_multiplier
    )

y.resize_out_img().save_out_img(path='../images/output.jpg', overwrite=True)
out_data=y.out_data
```


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job.)

[StackOverflow]: <https://stackoverflow.com/questions/30520666/pixelate-image-with-pillow>
