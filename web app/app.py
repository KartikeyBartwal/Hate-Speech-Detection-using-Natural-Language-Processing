from flask import Flask 

app = Flask("hate speech classification")

@app.route("/")
def hello_word():
    return "<p>Hello, World!</p>"