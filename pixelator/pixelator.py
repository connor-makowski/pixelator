import cv2, numpy, type_enforced


class Picture_Utils:
    @staticmethod
    def crop_image(image: list, width: int, height: int):
        """
        Crops an image to a specified width and height (centered)

        Takes in three required arguments:

            - 'image':
                - Type: list of lists
                - What: CV2 image data
            - 'width':
                - Type: int
                - What: The width in pixels for the output image
            - 'height':
                - Type: int
                - What: The height in pixels for the output image
        """
        (h, w) = image.shape[:2]
        if width > w or height > h:
            raise Exception("Cannot crop an image larger")
        h_start = (h - height) // 2
        h_end = h_start + height
        w_start = (w - width) // 2
        w_end = w_start + width
        return image[h_start:h_end, w_start:w_end]

    @staticmethod
    def crop_to_aspect_ratio(image: list, aspect_ratio_w_by_h: [int, float]):
        """
        Crops an image to a specified aspect ratio

        Takes in two required arguments:

            - 'image':
                - Type: list of lists
                - What: CV2 image data
            - 'aspect_ratio_w_by_h':
                - Type: int | float
                - What: The aspect ratio for the cropped image
        """
        (h, w) = image.shape[:2]
        aspect_ratio_current = w / h
        if aspect_ratio_w_by_h == aspect_ratio_current:
            return image
        new_h = int(w / aspect_ratio_w_by_h)
        new_w = int(h * aspect_ratio_w_by_h)
        if new_h < h:
            return Picture_Utils.crop_image(image, width=w, height=new_h)
        if new_w < w:
            return Picture_Utils.crop_image(image, width=new_w, height=h)
        raise Exception("Invalid aspect_ratio_w_by_h")

    @staticmethod
    def resize(
        image: list, width: int, height: int, interpolation=cv2.INTER_AREA
    ):
        """
        Resizes an image to a specified width and height

        Takes in three required arguments:

            - 'image':
                - Type: list of lists
                - What: CV2 image data
            - 'width':
                - Type: int
                - What: The width in pixels for the output image
            - 'height':
                - Type: int
                - What: The height in pixels for the output image
        """
        image = Picture_Utils.crop_to_aspect_ratio(image, width / height)
        return cv2.resize(image, (width, height), interpolation=interpolation)

    @staticmethod
    def quantize_to_palette(image: list, palette: list):
        """
        Quantizes an image to a given palette

        Takes in two required arguments:

            - 'image':
                - Type: list of lists
                - What: CV2 image data
            - 'palette':
                - Type: list of lists
                - What: A list of BGR lists for quantizing the image
        """
        image = image.astype(numpy.int16)
        quantized_image = numpy.zeros_like(image)
        palette = numpy.array(palette, dtype=numpy.int16)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                quantized_image[i, j] = palette[
                    numpy.argmin(
                        numpy.sum(
                            numpy.absolute((palette - image[i, j])), axis=1
                        )
                    )
                ]
        return quantized_image.astype(numpy.uint8)

    @staticmethod
    def capture(cam_port: int = 0):
        """
        Uses an attached camera or webcam to capture its input at the time of calling

        Takes in one optional argument:

            - 'cam_port':
                - Type: int
                - What: The camera port to use for a capture
                - Default: 0
                - Note: For more info see the docs for cv2.VideoCapture.
        """
        cam = cv2.VideoCapture(cam_port)
        try:
            result, image = cam.read()
            cam.release()
        except Exception as e:
            cam.release()
            raise Exception(e)
        return image

    @staticmethod
    def to_colorscheme(image: list, colorscheme: str = "bgr"):
        """
        Converts an image to an alternate colorscheme

        Takes in one required argument:

            - 'image':
                - Type: list of lists
                - What: CV2 image data

        Takes in one optional argument:

            - 'colorscheme':
                - Type: str
                - What: The color scheme to convert
                - Options: ['bgr', 'rgb', 'gray', 'hsv']
                - Default: 'bgr'

        """
        colorscheme = str(colorscheme).lower()
        if colorscheme == "bgr":
            return image
        if colorscheme == "rgb":
            return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if colorscheme == "gray":
            return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if colorscheme == "hsv":
            return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    @staticmethod
    def read(filename: str):
        """
        Reads a picture into CV2 image data

        Requires one argument:

            - 'filename':
                - Type: str
                - What: Filename from which to load a picture
        """
        return cv2.imread(filename)


@type_enforced.Enforcer
class Pixelator(Picture_Utils):
    def __init__(
        self,
        data: [numpy.ndarray, list, None] = None,
        filename: [str, None] = None,
        cam_port: int = 0,
    ):
        """
        Initialize a Pixelator object.

        Takes in three optional arguments:

            - 'data':
                - Type: list of lists
                - What: BGR array of data to input
                - Note: If not specified, proceeds to attempt to load from a filename
            - 'filename':
                - Type: str
                - What: Filename from which to load a picture
                - Note: If not specified, proceeds to attempt a camera capture
            - 'cam_port':
                - Type: int
                - What: The camera port to use for a capture
                - Note: For more info see the docs for cv2.VideoCapture.
        """
        if data is not None:
            self.data = data
        elif filename is not None:
            self.data = self.read(filename)
        else:
            self.data = self.capture(cam_port)

    def pixelate(
        self,
        width: [int, None] = None,
        height: [int, None] = None,
        palette: [numpy.ndarray, list, None] = None,
    ):
        """
        Pixelates an image to a specific shape and color palette

        Returns a new Pixelator (class) image

        Takes in three optional arguments:

            - 'width':
                - Type: int
                - What: The width in pixels for the output image
                - Note: If either 'width' or 'height' are not specified, this function only applies the palette
            - 'height':
                - Type: int
                - What: The height in pixels for the output image
                - Note: If either 'width' or 'height' are not specified, this function only applies the palette
            - 'palette':
                - Type: list of lists
                - What: A list of BGR lists to apply as a pallete
                - Note: If not specified, no palette is applied
        """
        out = self.resize(image=self.data, width=width, height=height)
        if palette is not None:
            out = self.quantize_to_palette(out, palette)
        return Pixelator(data=out)

    def write(
        self,
        filename: str,
        width: [int, None] = None,
        height: [int, None] = None,
    ):
        """
        Writes the current image to a specific file and resizes to a given width and height if supplied

        Takes in one required argument:

            - 'filename':
                - Type: str
                - What: Filename at which to write the picture

        Takes in two optional arguments:

            - 'width':
                - Type: int
                - What: The width in pixels for the output image
                - Note: If either 'width' or 'height' are not specified, no resizing is done
            - 'height':
                - Type: int
                - What: The height in pixels for the output image
                - Note: If either 'width' or 'height' are not specified, no resizing is done
        """
        if width == None or height == None:
            (height, width) = self.data.shape[:2]
        cv2.imwrite(
            filename, self.resize(self.data, width, height).astype(numpy.uint8)
        )

    def get_color_counts(self):
        """
        Gets the counts of each color in the image

        Returns a dictionary of color counts where:
            - The keys are the tuples of the colors
            - The values are the counts of each color

        EG: {(255, 255, 255): 100, (0, 0, 0): 50}
        """
        colors, count = numpy.unique(
            self.data.reshape(-1, self.data.shape[-1]),
            axis=0,
            return_counts=True,
        )
        # Force all items in colors to be integers
        colors = colors.astype(int)
        return dict(zip([tuple(color) for color in colors], count))
