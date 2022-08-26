from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Melhor sistema de protese do mundo"

if __name__ == '__main__':
    app.run()