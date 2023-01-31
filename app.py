from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__, template_folder="templates", static_folder="static")
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secretkey'


class User(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Routes defined here

# Route for homepage
@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html', title='Homepage')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

# App runs here
if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)