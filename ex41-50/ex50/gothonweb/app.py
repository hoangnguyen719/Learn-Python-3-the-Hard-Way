from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', 'Nobody')
    
    if name:
        greeting = f"Hello {name}"
    else:
        greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

@app.route('/1')
def index2():
    return render_template("foo.html")
    
if __name__ == "__main__":
    app.run()