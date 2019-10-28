from pixelator import pixelator
palette = [
    (45,  50,  50),  #black
    (240, 68,  64),  #red
    (211, 223, 223), #white
    (160, 161, 67),  #green
    (233, 129, 76),  #orange
]

sensitivity_multiplier = 10

size = (45,45)

y=pixelator(
    in_path='./images/input.jpg',
    palette=palette,
    size=size,
    sensitivity_multiplier=sensitivity_multiplier
    )

y.resize_out_img().save_out_img(path='./images/output.jpg', overwrite=True)
print (y.out_data)
