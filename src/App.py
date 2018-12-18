from flask import Flask, request, jsonify
from flask_cors import CORS
import random as rnd
import base64
import subprocess
#from main import main
app = Flask(__name__)
CORS(app)
from PIL import Image
from array import *
from .model import Model

@app.route("/")
def main():
    return "Literally nothing"

# Returns a random double in [0,1]
@app.route('/random')
def thisnameisrandom():
    return str(rnd.random())

# Test to determine passing parameters
@app.route('/test/<par>')
def printparam(par):
    return par

# Endpoint for POST request from React app
@app.route('/recieve', methods=['POST'])
def reciever():
    data = request.get_json()

    # Handles bad requests / empty data
    if data is None:
      print("No valid request body, json missing!")
      return jsonify({'error': 'No valid request body, json missing!'})
    else:
      img_data = data['img']
    successMessage = decodeb64(img_data)
    print(successMessage+"Resizing now:")
    subprocess.call("./src/resize-script.sh", shell=True)
    print("Resize complete.")
    #return imageManipAndPredict
    data = {'val': 'test'}
    return jsonify(data)
    #return
      

def decodeb64(str):
    #You pass a string to img_data
    img_data = str
    #Get rid of the byte header data:image/png;base64
    img_data= img_data.replace('data:image/png;base64,', '')

    #Change it into byte form  b'string'
    img_data= img_data.encode()

    #if you want to change file type to .png just change testPic.jpg to testPic.png
    fh = open("input.jpg", "wb")
    fh.write(base64.b64decode(img_data))
    fh.close()
    return "input.jpg saved successfully. "


def imageManipAndPredict():
    # IMAGE MANIP
    img = Image.open('scaledinput.png').convert('LA')
    img.save('grayscaledinput.png')

    file = 'grayscaledinput.png'

    data_image = array('B')

    Im = Image.open(file)
    pixel = Im.load()
    width, height = Im.size

    untupled_pixels = [[0 for x in range(28)] for y in range(28)]

    for x in range(28):
        for y in range(28):
            untupled_pixels[x][y] = pixel[x, y][0]

    for x in range(0, width):
        for y in range(0, height):
            # if (untupled_pixels[x][y] < 150):
            #     untupled_pixels[x][y] = 0
            data_image.append(int(127.5 - (float(untupled_pixels[y][x]) - 127.5)))
            print(str(int(127.5 - ((float(untupled_pixels[y][x])) - 127.5))) + "\t", end="")
        print("")

    hexval = "{0:#0{1}x}".format(1, 6)

    header = array('B')
    header.extend([0, 0, 8, 1, 0, 0])
    header.append(int('0x' + hexval[2:][:2], 16))
    header.append(int('0x' + hexval[2:][2:], 16))

    header.extend([0, 0, 0, width, 0, 0, 0, height])
    header[3] = 3  # New MSB (image data) 0x00000803

    data_image = header + data_image

    output_file = open('inputdata-images-idx3-ubyte', 'wb')
    data_image.tofile(output_file)
    output_file.close()

    # os.system('gzip inputdata-images-idx3-ubyte') #don't need to rezip

    # MODEL
    mydigits = Model()
    mydigits.load()
    return mydigits.predict()

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8000)