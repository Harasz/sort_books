from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from configparser import ConfigParser
from functools import wraps
import psycopg2
import secure


app = Flask(__name__)
api = Api(app=app, prefix='/api')

auth_k = []
parser = reqparse.RequestParser()

conf = ConfigParser()
conf.read(filenames='./server.cfg')


def print_error(e):
	print("[ERROR] "+str(e))
	print("API kończy pracę")
	exit(0)

try:
	Sec = secure.Secure()
except Exception as e:
	print_error(e)


try:
	conn = psycopg2.connect(dbname=conf['SERVER_SQL']['Database'],
							user=conf['SERVER_SQL']['User'],
							host=conf['SERVER_SQL']['Address'],
							password=conf['SERVER_SQL']['Password'])
	conn.autocommit = True
	cur = conn.cursor()
except Exception as e:
	print_error(e)


def login_required(data):
		if data['key'] in [x[0] for x in auth_k]:
			return True
		return False
