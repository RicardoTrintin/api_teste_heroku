from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return f"""testando envs {os.environ.get("teste")}"""

if __name__ == '__main__':
    app.run()