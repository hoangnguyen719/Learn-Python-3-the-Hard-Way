import os
from flask import Flask, flash, render_template, request, redirect, url_for, escape
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.instance_path, 'upload')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1).lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        greeting = request.form['greeting']
    else:
        greeting = None
    return render_template("index.html", greeting=greeting)

@app.route('/login', methods=['POST', 'GET'])
def login():
    username = 'admin'
    password = '123'
    error = None  
    if request.method == "POST":
        if (request.form['username'] != username) or (request.form['password'] != password):
            error = "Invalid username or password!"
        else:
            message = "Successfully logged in! Loading..."
            seconds = 1.5
            redirect_url = "/upload/" + username
            return redirect(url_for('redirecting', message=message, seconds=seconds, redirect_url=redirect_url))
            # return render_template("index.html", greeting = "Hello " + username)
    return render_template("login.html", error=error)

@app.route('/redirecting', methods=['GET', 'POST'])
def redirecting():
    message = request.args.get('message')
    seconds = request.args.get('seconds')
    redirect_url = request.args.get('redirect_url')
    return render_template("redirect.html", message=message, seconds=seconds, redirect_url=redirect_url)

@app.route("/upload/<string:username>", methods=['POST', 'GET'])
def upload(username):
    if request.method == 'POST':
        return "Upload photo"
    else:
        return render_template("upload.html", username=username)

@app.route("/user/<username>")
def show_user_profile(username):
    return 'User %s' % escape(username)
    
# if __name__ == "__main__":
#     app.run(debug=True)

# to run flask app, type (in PowerShell):
# $env:FLASK_APP="<name of flask app>"
# $env:FLASK_ENV="development" <----- if want to run in debug mode
# flask run -----OR----- python -m flask run