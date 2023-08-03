from pixelator import Pixelator
# Use the input filename provided
image = Pixelator(filename='./images/input.jpg')
# Define a custom palette
palette = [
    [50,50,45],     #black
    [64,68,240],    #red
    [223,223,211],  #white
    [67,161,160],   #green
    [76,129,233],   #orange
]


# Pixelate the image to a 28x28 black and white array
pixelated_image = image.pixelate(
    width=28,
    height=28,
    palette=palette
)
# Write to `output.png` scaled up to a 500x500 image (to be easily viewed)
pixelated_image.write(filename='./images/output_test_2.jpg', width=300, height=300)
# Test that the color counts are correct
color_counts = pixelated_image.get_color_counts()
expected_color_counts = {(50, 50, 45): 248, (64, 68, 240): 8, (67, 161, 160): 394, (76, 129, 233): 104, (223, 223, 211): 30}
assert color_counts == expected_color_counts, "Expected color counts is not correct for test_2.py"