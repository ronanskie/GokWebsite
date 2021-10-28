#! /usr/bin/env python3

import os
import sys
import sqlite3
from sqlite3 import Error

class DB:

	#connection to database created
	def createConnection(self, conn):
  		#location of database
		database = r"../db/main.db" 
		
		# create a database connection if necessary
		if conn is None or not conn:
			try:
				conn = sqlite3.connect(database) #setting this to false might give issues
				print("New connection with database established")
			except Error as e:
				print(e)

		return conn