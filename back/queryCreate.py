#! /usr/bin/env python3

import os
import sys
import sqlite3
from sqlite3 import Error

class queryCreater:

	#creates a query for getting a value
	def createSetQuery(self, column, value):
		query = "UPDATE morris SET " + column + "=" + str(value) + " WHERE mid=0" 
		return query
	
	#creates a query for setting value
	def createGetQuery(self, column):
		query = "SELECT " + column + " FROM morris WHERE mid=0"
		return query