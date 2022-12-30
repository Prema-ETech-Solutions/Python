from flask import Flask,request
import json

app = Flask(__name__)
@app.route('/scrap')
def start():
    dataCollection = []
    link = request.args.get("link")
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True)                    