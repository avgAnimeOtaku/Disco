from PIL import Image


width, height = 1920, 1080

# Create a new image with a black background
image = Image.new(mode='RGB', size=(width, height), color=(0, 0, 0))


# Loop through every pixel and set a random RGB value
for x in range(width):
    for y in range(height):
        image.putpixel((x, y), (r, g, b))