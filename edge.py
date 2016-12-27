from PIL import Image, ImageFilter

img = Image.open('kirin.jpg')
filtered = img.filter(ImageFilter.FIND_EDGES)
filtered.save('kirin_edge.jpg')