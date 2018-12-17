from flask import Flask
import random as rnd

app = Flask(__name__)

@app.route("/")
def main():
    return "Literally nothing"

@app.route('/random')
def thisnameisrandom():
    return str(rnd.random())

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8000)