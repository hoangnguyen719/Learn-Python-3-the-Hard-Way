from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()