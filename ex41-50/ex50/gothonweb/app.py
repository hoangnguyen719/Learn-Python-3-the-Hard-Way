import os
from flask import Flask, flash, render_template, request, redirect, url_for, escape, send_from_directory
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = os.path.join('static', 'image')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        greeting = request.form['greeting']
    else:
        greeting = None
    return render_template("index.html", greeting=greeting)

@app.route("/login", methods=['POST', 'GET'])
def login():
    username = 'admin'
    password = '123'
    error = None  
    if request.method == 'POST':
        if (request.form['username'] != username) or (request.form['password'] != password):
            error = "Invalid username or password!"
        else:
            message = "Successfully logged in!"
            seconds = 1.5
            redirect_url = "/upload/" + username
            return redirect(url_for('redirecting', message=message, seconds=seconds, redirect_url=redirect_url))
            # return render_template("index.html", greeting = "Hello " + username)
    return render_template("login.html", error=error)

@app.route("/redirecting", methods=['GET', 'POST'])
def redirecting():
    message = request.args.get('message')
    seconds = request.args.get('seconds')
    redirect_url = request.args.get('redirect_url')
    return render_template("redirect.html", message=message, seconds=seconds, redirect_url=redirect_url)

@app.route("/upload/<string:username>", methods=['POST', 'GET'])
def upload(username):
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file part!")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash("No selected file!")
            return redirect(request.url)
        elif file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = app.config['UPLOAD_FOLDER']
            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)
            return redirect(url_for('uploaded', filename=filename, filepath=filepath,\
                upload_folder = upload_folder, username=username))
    else:
        return render_template("upload.html", username=username)

@app.route("/uploaded")
def uploaded():
    filename = request.args.get('filename')
    filepath = request.args.get('filepath')
    upload_folder = request.args.get('upload_folder')
    username = request.args.get('username')
    # return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    return render_template("uploaded.html", filename=filename, filepath=filepath,\
        upload_folder = upload_folder, username=username)

@app.route("/user/<username>")
def show_user_profile(username):
    return 'User %s' % escape(username)
    
# if __name__ == "__main__":
#     app.run(debug=True)

# to run flask app, type (in PowerShell):
# $env:FLASK_APP="<name of flask app>"
# $env:FLASK_ENV="development" <----- if want to run in debug mode
# flask run -----OR----- python -m flask run