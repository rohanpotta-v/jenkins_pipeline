from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, This is production!"

@app.route('/staging')
def hello():
    return "Hello, This is Staging!"

@app.route('/staging')
def hello():
    return "Hello, This is Devlopment!"
if __name__ == '__main__':
    app.run(debug=True)
