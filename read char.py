with open('main.py', 'rb') as file:
    byte_count = 0
    while True:
        byte = file.read(1)
        if not byte:
            break
        print(format(ord(byte), '08b'), end=' ')
        byte_count += 1
        if byte_count % 3 == 0:
            print()
