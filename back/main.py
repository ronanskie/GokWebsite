#! /usr/bin/env python3

#import some stuff
import os
from flask import Flask, render_template, request, flash, redirect, url_for, session #flask framework
import sqlite3 

template_dir = os.path.abspath('../front/templates') #setting path to template directory
static_dir = os.path.abspath('../front/static') #setting path to static directory
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir) #sets new directory for templates (html files etc.)
app.config['SECRET_KEY'] = 'gkwemfewown' #setting secret key

@app.route('/', methods=['GET', 'POST'])
def login():
	return render_template("login.html")

if __name__ == "__main__":
	app.run(debug=True)