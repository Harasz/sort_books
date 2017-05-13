from flask import Flask, request
from flask_restful import Resource
from sort_api import cur, login_required, parser, Sec, auth_k


class API_librariansInfo(Resource):

	def post(self):
		
		data = Sec.encode_data(parser.parse_args())	
		
		if not login_required(data):
			return {'status': 'brak autoryzacji'}, 401
		
		user_id = str([x[1] for x in auth_k if x[0]==data['key']][0])
		
		if not user_id:
			return {'status': 'brak autoryzacji'}, 401
		
		
		try:
			cur.execute("SELECT imie, nazwisko, email, master FROM librarians.user WHERE id=%s;", (user_id, ))
			resp = cur.fetchone()
			if resp:
				pub = open('pem/'+data['key']+'.pem', 'rb').read()
				return {'data': [Sec.encrypt_(str(value), pub) for value in resp]}, 200
			else:
					return {'status': 'brak danych'}, 204
		except Exception:
			return {'status': 'wystapil blad'}, 500
