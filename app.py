from flask import Flask, render_template, request, redirect, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

app.secret_key = "change-this-secret-key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register_user', methods=['POST'])
def register_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return "Email already registered"

    hashed_password = generate_password_hash(password)

    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect('/')


@app.route('/login_user', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        session['username'] = user.username
        return redirect('/dashboard')

    return "Invalid Email or Password"


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    files = os.listdir(app.config['UPLOAD_FOLDER'])

    return render_template(
        'dashboard.html',
        files=files,
        username=session['username']
    )


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'user_id' not in session:
        return redirect('/')

    if 'file' not in request.files:
        return redirect('/dashboard')

    file = request.files['file']

    if file.filename == '':
        return redirect('/dashboard')

    allowed_extensions = ['pdf', 'jpg', 'jpeg', 'png', 'docx', 'txt', 'zip']

    extension = file.filename.rsplit('.', 1)[-1].lower()

    if extension not in allowed_extensions:
        return "File type not allowed"

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    return redirect('/dashboard')


@app.route('/download/<filename>')
def download_file(filename):
    if 'user_id' not in session:
        return redirect('/')

    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename,
        as_attachment=True
    )


@app.route('/delete/<filename>')
def delete_file(filename):
    if 'user_id' not in session:
        return redirect('/')

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if os.path.exists(filepath):
        os.remove(filepath)

    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )