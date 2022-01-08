from flask import Flask
app = Flask(__name__)

print(__name__)

def make_bold(function):
    def wrapper():
        return '<b>' + function() + '</b>'
    return wrapper

def make_emphasis(function):
    def wrapper():
        return '<em>' + function() + '</em>'
    return wrapper

def make_underlined(function):
    def wrapper():
        return '<u>' + function() + '</u>'
    return wrapper




#If you have single quotes on the outside, ensure you have double quotes inside
@app.route("/")
def hello():
    return '<h1 style="text-align: center">Hello World!</h1>'\
            '<p>I wanted to slap you</p>'\
                '<img src="https://media.giphy.com/media/sBlmCCYAuAcNSq6yA6/giphy.gif" width=200>'

@app.route("/dex")
def dex():
    return "Dexter"


@app.route("/<name>")
def greet(name):
    return f'Hello there {name}'


@app.route("/user/<name>/<int:number>")
def greet1(name, number):
    return f'Happy {number}th birthday, {name}'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"





if __name__ == "__main__":
    app.run(debug = True)
