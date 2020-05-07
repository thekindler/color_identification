import os
from io import BytesIO
from urllib.request import urlopen
import colorz
import svgwrite
from PIL import Image
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/color-spectrum',methods = ['POST'])
def colorspectrum():
    body = request.get_json()
    img_url = body['img_url']

    # check if the image url is local or network and open accordingly
    img_fd = open(img_url, 'rb') if os.path.isfile(img_url) else \
        BytesIO(urlopen(img_url).read())

    # Image._show(image) # uncomment to display the image

    colors = colorz.colorz(img_fd) # call colors library
    result = []
    for c in colors:
        result.append(colorz.hexify(c[0]))
        result.append(colorz.hexify(c[1]))

    return jsonify(result)

@app.route('/api/color-spectrum-image',methods = ['POST'])
def colorspectrumimage():
    body = request.get_json()
    img_url = body['img_url']

    # check if the image url is local or network and open accordingly
    img_fd = open(img_url, 'rb') if os.path.isfile(img_url) else \
        BytesIO(urlopen(img_url).read())

    colors = colorz.colorz(img_fd)

    # TODO : create a jpeg image as svg supports only 16*16 format
    # note only a maximum of 16 colors can be shown in svg image
    dwg = svgwrite.Drawing('colour_spectrum.svg', profile='full')

    for i in range(0,len(colors)*2,2):
        j = int(i/2)
        dwg.add(dwg.line((0, 0 + i), (16, 0 + i),
                         stroke=svgwrite.rgb(colors[j][0][0], colors[j][0][1], colors[j][0][2], '%')))
        dwg.add(dwg.line((0, 0 + i+1), (16, 0 + i+1),
                         stroke=svgwrite.rgb(colors[j][1][0], colors[j][1][1], colors[j][1][2], '%')))

    dwg.save()
    img_fd = open('colour_spectrum.svg')
    encoded = base64.b64encode(open("colour_spectrum.svg", "rb").read())

    result = {}
    result['imageb64'] = encoded
    return jsonify(result)

if __name__ == '__main__':
   app.run()

# https://cdn.mos.cms.futurecdn.net/42E9as7NaTaAi4A6JcuFwG-320-80.jpg
# file:///home/anupam/workspaces/pycharm/colour_spectrum/apple.jpeg