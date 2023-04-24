with open("main.py", "rb") as file:
    for chunk in iter(lambda: file.read(3), b""):
        r, g, b = memoryview(chunk)
        print(r, g, b, end=" ")
        print()