from pixelator import Pixelator

# If the os is a docker image, exit the program
import os

if os.path.exists("/.dockerenv"):
    print("Test 3 skipped (cannot run in docker)")
    exit()

# Capture from a webcam since no data or filename is provided
image = Pixelator()

# Pixelate the image to a 28x28 black and white array
pixelated_image = image.pixelate(
    width=64,
    height=64,
    palette=[
        [0, 0, 0],
        [80, 80, 80],
        [160, 160, 160],
        [200, 200, 200],
        [255, 255, 255],
    ],
)
# Write to `output.png` scaled up to a 500x500 image (to be easily viewed)
pixelated_image.write(
    filename="./images/output_test_3.jpg", width=300, height=300
)

print("Test 3 passed")
