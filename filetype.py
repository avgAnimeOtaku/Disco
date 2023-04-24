import mimetypes

mimetypes.init()

filename = "main.py"
content_type = mimetypes.guess_type(filename)[0]
if content_type is not None:
    extension = mimetypes.guess_extension(content_type)
    print(extension)
else:
    print("Unknown file type")
