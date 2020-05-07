import os
from io import BytesIO
from urllib.request import urlopen
from PIL import Image
import colorz

image_filename = 'apple.jpeg'
img_fd = open(image_filename, 'rb') if os.path.isfile(image_filename) else \
    BytesIO(urlopen(image_filename).read())
image = Image.open(img_fd)

if __name__ == '__main__':
    colors = colorz.colorz(img_fd)
    print(colors)

    result = []
    for c in colors:
        result.append(colorz.hexify(c[0]))
        result.append(colorz.hexify(c[1]))

    print(result)
    html_fd = colorz.html_preview(colors,bg_img=None)
    html_url = 'file://'+html_fd.name
    print(html_url)