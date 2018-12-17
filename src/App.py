from flask import Flask, request, jsonify
from flask_cors import CORS
import random as rnd
import base64
import subprocess

app = Flask(__name__)
CORS(app)

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
    subprocess.call("resize-script.sh", shell=True)
    print("Resize complete.")
    return
      

def decodeb64(str):
    #You pass a string to img_data
    img_data = str
    #Get rid of the byte header data:image/png;base64
    img_data= img_data.replace('data:image/png;base64,', '')

    #Change it into byte form  b'string'
    img_data= img_data.encode()

    #if you want to change file type to .png just change testPic.jpg to testPic.png
    fh = open("./data/input.jpg", "wb")
    fh.write(base64.b64decode(img_data))
    fh.close()
    return "./data/input.jpg saved successfully. "

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8000)