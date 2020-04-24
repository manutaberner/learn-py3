import requests
from io import BytesIO
from PIL import Image

r = requests.get('https://pngimage.net/wp-content/uploads/2018/06/png-wallpaper-2.png')

print('Status code:', r.status_code)

image = Image.open(BytesIO(r.content))



print(image.size, image.format, image.mode)
path = './image.' + image.format

try: 
    image.save(path, image.format)
except IOError:
    print('Cannot save Image')
    