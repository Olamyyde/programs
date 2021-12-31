from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dex")
def dex():
    return "Dexter"



if __name__ == "__main__":
    app.run()