from flask import Flask, request
from flask_restful import Resource
from sort_api import cur, login_required, parser, Sec
from hashlib import sha512
import random


class API_addLibrarians(Resource):
			
	def post(self):
		
		data = Sec.encode_data(parser.parse_args())
		
		if not login_required(data):
			return {'status': 'brak autoryzacji'}, 401

		try:
			name = data['arg1'].split('/')
			cur.execute("SELECT * FROM librarians.user WHERE imie=%s AND nazwisko=%s AND email=%s;",
						(name[0], name[1], data['arg2']))
			resp = cur.fetchall()
			if resp:
				return {'status': 'istnieje'}, 507
			else:
				if data['arg3'] == 'True': data['arg3']='1'
				else: data['arg3']='0'
			
				password = ''.join(random.sample('qwertyuiopasdfghjklzxcvbnm1234567890', 8))
				cur.execute("INSERT INTO librarians.user VALUES (default, %s, %s, %s, %s, %s);",
							(name[0], name[1], data['arg2'],
							sha512(password.encode('UTF-8')).hexdigest(), data['arg3']))
				pub = open('pem/'+data['key']+'.pem', 'rb').read()
				return {'status': 'dodano', 'data': Sec.encrypt_(password, pub)}, 201
		except Exception:
			return {'status': 'wystapil blad'}, 500
