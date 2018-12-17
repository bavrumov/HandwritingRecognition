from flask import Flask, request, jsonify
from flask_cors import CORS
import random as rnd
import base64

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    return "Literally nothing"

@app.route('/random')
def thisnameisrandom():
    return str(rnd.random())

@app.route('/test/<par>')
def printparam(par):
    return par

@app.route('/recieve', methods=['POST'])
def reciever():
    data = request.get_json()
    if data is None:
      print("No valid request body, json missing!")
      return jsonify({'error': 'No valid request body, json missing!'})
    else:
      img_data = data['img']
    return decodeb64(img_data)
      

def decodeb64(str):
    #You pass a string to img_data
    img_data = str
    #Get rid of the byte header data:image/png;base64
    img_data= img_data.replace('data:image/png;base64,', '')

    #Change it into byte form  b'string'
    img_data= img_data.encode()

    #if you want to change file type to .png just change testPic.jpg to testPic.png
    fh = open("output.jpg", "wb")
    fh.write(base64.b64decode(img_data))
    fh.close()
    return "output.jpg saved successfully"

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8000)