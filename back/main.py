#! /usr/bin/env python3

#import some stuff
import os
from flask import Flask, render_template, request, flash, redirect, url_for, session #flask framework
import sqlite3 
from db import DB
from mainAssist import Assist

template_dir = os.path.abspath('../front/templates') #setting path to template directory
static_dir = os.path.abspath('../front/static') #setting path to static directory
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir) #sets new directory for templates (html files etc.)
app.config['SECRET_KEY'] = 'gkwemfewown' #setting secret key

dataB = DB() #creates instance of database
conn = dataB.createConnection() #creates connection with database

#login page
@app.route('/', methods=['GET', 'POST'])
def login():

	if request.method == "POST":
		#login submit button
		if request.form.get("action") == "login":
			username = request.form["username"] #gets username and password when user submits them
			password = request.form["password"]

			if Assist.loginCheck(username, password, dataB, conn) is True:
				print("The following user has been logged in:" + username + "(" + password + ")")
				return redirect(url_for("home"))

		#register submit button
		elif request.form.get("action") == "register":
			username = request.form["username"] #gets username and password when user submits them
			password = request.form["password"]

			#checks if username is valid so it can be registered
			if Assist.registerCheck(username, dataB, conn) is True:
				newUid = Assist.newUid(dataB, conn)
				print(newUid)
				dataB.insertRow(newUid, password, username, conn)
				print("The following user has been registered " + username + "(" + password + ")")

	return render_template("login.html")

#home page
@app.route('/home', methods=['GET', 'POST'])
def home():

	return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True)
