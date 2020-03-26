from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/hello', methods=['POST', 'GET'])
# def hello():
#     greeting = "Hello World"
    
#     if request.method == "POST":
#         name = request.form['name']
#         greet = request.form['greet']
#         greeting = f"{greet}, {name}"
#         return render_template("index.html", greeting=greeting)
#     else:
#         return render_template("hello_form.html")

# @app.route("/user/<username>")
# def show_user_profile(username):
#     return 'User %s' % escape(username)
    
if __name__ == "__main__":
    app.run(debug=True)