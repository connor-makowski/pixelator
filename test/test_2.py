from pixelator import Pixelator

# Use the input filename provided
image = Pixelator(filename="./images/input.jpg")
# Define a custom palette
palette = [
    [0, 0, 0],  # black
    [50, 50, 45],  # darkgrey
    [244, 169, 245],  # pink
    [223, 223, 211],  # white
    [134, 171, 209],  # brown
]

# Pixelate the image to a 28x28 black and white array
pixelated_image = image.pixelate(width=28, height=28, palette=palette)
# Write to `output.png` scaled up to a 300x300 image (to be easily viewed)
# pixelated_image.write(filename='./images/output_test_2.jpg', width=300, height=300)

# Test that the color counts are correct
color_counts = pixelated_image.get_color_counts()
expected_color_counts = {
    (0, 0, 0): 360,
    (50, 50, 45): 163,
    (134, 171, 209): 168,
    (223, 223, 211): 93,
}
assert (
    color_counts == expected_color_counts
), "Expected color counts is not correct for test_2.py"
print("Test 2 passed")
