from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Agora os guaipecas estao vendo"

if __name__ == '__main__':
    app.run()