#! /usr/bin/env python3

#import some stuff
import os
from flask import Flask, render_template, request, flash, redirect, url_for, session #flask framework
import sqlite3 
from db import DB

class Assist:



	#returns new uid for registering new user
	def newUid(self, dataB, conn):
		uid = dataB.getValue(0, 1, 0, conn) + 1
		return uid

