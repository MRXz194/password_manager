#################################################
# Built by MRX 2024
# chill project
# github: https://github.com/MRXz194   Discord: kz5198
##################################################
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load bien mtrng(lmao)
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-123')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# In/ load encrp key
def get_key():
    key_file = 'key.key'
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
        return key

cipher_suite = Fernet(get_key())

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    passwords = db.relationship('Password', backref='owner', lazy=True)

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    encrypted_password = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def get_password(self):
        return cipher_suite.decrypt(self.encrypted_password.encode()).decode()

    def set_password(self, password):
        self.encrypted_password = cipher_suite.encrypt(password.encode()).decode()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_password():
    if request.method == 'POST':
        site = request.form.get('site')
        username = request.form.get('username')
        password = request.form.get('password')

        if site and username and password:
            new_password = Password(site=site, username=username, user_id=current_user.id)
            new_password.encrypted_password = cipher_suite.encrypt(password.encode()).decode()
            db.session.add(new_password)
            db.session.commit()
            flash('Password added successfully!', 'success')
            return redirect(url_for('dashboard'))
        
        flash('Please fill in all fields', 'error')
    return redirect(url_for('dashboard'))

@app.route('/delete/<int:id>')
@login_required
def delete_password(id):
    password = Password.query.get_or_404(id)
    if password.user_id != current_user.id:
        flash('Access denied', 'error')
        return redirect(url_for('index'))
    
    db.session.delete(password)
    db.session.commit()
    flash('Password deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
@login_required
def dashboard():
    passwords = Password.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', passwords=passwords)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('index'))
            
        flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
            
        new_user = User(username=username, password_hash=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8080, debug=True)
