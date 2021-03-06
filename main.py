from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pyth2468@localhost/expense'
db = SQLAlchemy(app)


@app.route('/')
def login():
	return render_template('login.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/login_validation', methods=['Post'])
def login_validation():
	email=request.form.get('email')
	password=request.form.get('password')

	return"""SELECT * FROM `users` WHERE `email` LIKE {} AND `password` LIKE {}""".format(email,password)

if __name__=="__main__":
	app.run(debug=True)