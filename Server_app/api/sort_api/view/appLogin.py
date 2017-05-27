from flask import Flask, request
from flask_restful import Resource
from hashlib import sha512
from sort_api import cur, auth_k, parser, Sec
import random
from datetime import date
from datetime import datetime


class API_appLogin(Resource):

	def post(self):

		data = Sec.encode_data(parser.parse_args())
		
		try:
			pass_ = sha512(data['pass_'].encode()).hexdigest()
			cur.execute("SELECT * FROM librarians.user WHERE email=%s AND haslo=%s;", (data['login'].lower(), pass_))
			resp = cur.fetchone()
			if resp:
				d = date.today() - resp[6]
				if d.days >= 30:
					d = '1'
				else:
					d = '0'
				cache = ''.join(random.sample('qwertyuiopasdfghjklzxcvbnm123456789', 32))
				auth_k.append((cache, resp[0]))
				open('pem/'+cache+'.pem', 'wb').write(data['publicKey'])

				return {'auth': Sec.encrypt_(cache, Sec.get_public()),
						'master': Sec.encrypt_(str(resp[5]), data['publicKey']),
						'data': Sec.encrypt_(d, data['publicKey'])}, 200
			else:
				return {'status': 'zle dane'}, 406
		except:
			return {'status': 'blad'}, 500
