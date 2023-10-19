from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask World!'

if __name__ == '__app__':
    app.run(host="0.0.0.0", port=5051)