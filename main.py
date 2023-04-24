from PIL import Image

width, height = 1920, 1080

frame = 0
image = Image.new(mode='RGB', size=(width, height), color=(0, 0, 0))

x, y = 0, 0
with open("main.py", "rb") as file:
    for chunk in iter(lambda: file.read(3), b""):
        mv = memoryview(chunk)
        r = mv[0] if len(mv) > 0 else 0
        g = mv[1] if len(mv) > 1 else 0
        b = mv[2] if len(mv) > 2 else 0
        image.putpixel((x, y), (r, g, b))
        if x == width - 1 and y == height - 1:
            image.save("frames/frame" + frame + ".png")
            x, y = 0, 0
            frame += 1