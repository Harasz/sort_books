from flask import Flask, request
from flask_restful import Resource
from sort_api import cur, auth_k, parser, Sec
from hashlib import sha512
import random


class API_addRe(Resource):
			
	def post(self):
		
		data = Sec.encode_data(parser.parse_args())
		
		if not data['key'] in auth_k:
			return {'status': 'brak autoryzacji'}, 401

		try:
			cur.execute("SELECT * FROM librarians.readers WHERE name=%s AND addres=%s;", (data['arg1'], data['arg2']))
			resp = cur.fetchall()
			if resp:
				return {'status': 'istnieje'}, 507
			else:
				password = ''.join(random.sample('qwertyuiopasdfghjklzxcvbnm1234567890', 8))
				cur.execute("INSERT INTO librarians.readers VALUES (default ,%s, %s, 'null', %s, 'false', %s);", (data['arg1'], data['arg2'], sha512(password.encode('UTF-8')).hexdigest(), data['login']))
				pub = open('pem/'+data['key']+'.pem', 'rb').read()
				return {'status': 'dodano', 'login': Sec.encrypt_(data['arg1'], pub), 'haslo': Sec.encrypt_(password, pub)}, 201
		except Exception as e:
			return {'status': Sec.encrypt_(str(e), open('pem/'+data['key']+'.pem', 'rb').read())}, 500
