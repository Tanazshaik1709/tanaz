from flask import Flask, render_template, request, redirect, url_for, session
'''from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'agency'
mysql = MySQL(app)'''
app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def login():
	return render_template('login.html', msg='')
'''
@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
     	return render_template('login.html')'''
@app.route('/register/', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
@app.route('/book/', methods=['GET', 'POST'])
def book():
    return render_template('book.html')
@app.route('/hotel/')
def hotel():
    return render_template('hotel.html')
@app.route('/car/')
def car():
    return render_template('car.html')
@app.route('/car1/')
def car1():
    return render_template('car1.html')
if __name__ == '__main__':
    app.run(debug=True)
