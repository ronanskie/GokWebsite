#! /usr/bin/env python3

#import some stuff
import os
from flask import Flask, render_template, request, flash, redirect, url_for, session #flask framework
import sqlite3 
from db import DB

class Assist:

	#returns new uid for registering new user
	def newUid(dataB, conn):
		uid = dataB.getValue(0, 0, 1, 0, conn) + 1
		return uid

	#checks if username is valid and not used, returns true if username can be used
	def registerCheck(username, dataB, conn):
		userFound = dataB.getValue("username", "username", 0, username, conn)

		if userFound is None:
			return True

		else:
			return False

	#checks if login credentials are valid
	def loginCheck(username, password, dataB, conn):
		if dataB.getValue("password", "username", 0, username, conn) is None:
			return False

		else:
			return True


