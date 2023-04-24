with open('main.py', 'rb') as file:
    binary_data = file.read()
    for byte in binary_data:
        print(format(byte, '08b'))

with open("main.py", "rb") as file:
    for chunk in iter(lambda: file.read(3), b""):
        mv = memoryview(chunk)
        r = mv[0] if len(mv) > 0 else 0
        g = mv[1] if len(mv) > 1 else 0
        b = mv[2] if len(mv) > 2 else 0