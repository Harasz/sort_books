from flask import Flask, request
from flask_restful import Resource
from hashlib import sha512
from sort_api import cur, auth_k, parser, Sec, login_required
from datetime import date


class API_librariansPass(Resource):

	def post(self):

		data = Sec.encode_data(parser.parse_args())
		
		if not login_required(data):
			return {'status': 'brak autoryzacji'}, 401
			
		user_id = str([x[1] for x in auth_k if x[0]==data['key']][0])
		
		if not user_id:
			return {'status': 'brak autoryzacji'}, 401
		
		try:
			pass_old = sha512(data['arg1'].encode()).hexdigest()
			cur.execute("SELECT haslo FROM librarians.user WHERE id=%s;", (user_id, ))
			resp = cur.fetchone()
			
			if resp[0] == pass_old:
				pass_new = sha512(data['pass_'].encode()).hexdigest()
				data = date.today()
				cur.execute("UPDATE librarians.user SET haslo=%s, last=%s WHERE id=%s;", (pass_new, data.isoformat(), user_id))
				return {'status': 'zmieniono'}, 200
			else:
				return {'status': 'rozne'}, 409
		except:
			return {'status': 'blad'}, 500
