from flask import Flask, render_template, request, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        nullable=False
    )

    password = db.Column(
        db.String(100),
        nullable=False
    )


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login_user', methods=['POST'])
def login_user():

    email = request.form['email']

    password = request.form['password']

    user = User.query.filter_by(
        email=email,
        password=password
    ).first()

    if user:
        return redirect('/dashboard')

    else:
        return "Invalid Email or Password"


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register_user', methods=['POST'])
def register_user():

    username = request.form['username']

    email = request.form['email']

    password = request.form['password']

    new_user = User(
        username=username,
        email=email,
        password=password
    )

    db.session.add(new_user)

    db.session.commit()

    return redirect('/')


@app.route('/dashboard')
def dashboard():

    files = os.listdir(
        app.config['UPLOAD_FOLDER']
    )

    return render_template(
        'dashboard.html',
        files=files
    )


@app.route('/upload', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        return redirect('/dashboard')

    file = request.files['file']

    if file.filename == '':
        return redirect('/dashboard')

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    return redirect('/dashboard')


@app.route('/download/<filename>')
def download_file(filename):

    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename,
        as_attachment=True
    )


@app.route('/delete/<filename>')
def delete_file(filename):

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        filename
    )

    if os.path.exists(filepath):
        os.remove(filepath)

    return redirect('/dashboard')


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )