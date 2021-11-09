#! /usr/bin/env python3

import os
import sys
import sqlite3
from sqlite3 import Error

class queryCreater:

	#creates a query for setting a value
	def createSetQuery(column, value, uid):
		query = 'UPDATE users SET ' + column + ' = ' + str(value) + ' WHERE uid = ' + str(uid) + ';'
		return query
	
	#creates a query for getting value. rowNr is amount of rows returned (0 if not applicable). column is column that has to be returned. value is to find correct row
	def createGetQuery(column, column2, rowNr, value):
		if rowNr != 0:
			query = 'SELECT uid FROM users ORDER BY uid DESC LIMIT ' + str(rowNr) + ';'
			return query

		else:
			query = 'SELECT ' + column + ' FROM users WHERE ' + column2 + ' = "' + str(value) + '";'
			return query

	#creates a query for inserting rows into "users" table
	def createInsertQuery(uid, password, username):
		query = 'INSERT INTO users (uid, password, username, coins, betNum, betEO, betNumAmount, betEOAmount) VALUES ("' + str(uid) + '", "' + str(password) + '", "' + str(username) + '", 1000, 0, 0, 0, 0);'
		return query