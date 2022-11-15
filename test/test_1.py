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
