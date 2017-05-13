from flask import Flask, request
from flask_restful import Resource
from sort_api import cur, login_required, parser, Sec


class API_showComm(Resource):
			
	def post(self):
		
		data = Sec.encode_data(parser.parse_args())	
		
		if not login_required(data):
			return {'status': 'brak autoryzacji'}, 401
		
		try:
			cur.execute("SELECT id_comment, comment, r_name FROM librarians.comments WHERE accept='0';")
			resp = cur.fetchall()
			if resp:
				ret = {}
				pub = open('pem/'+data['key']+'.pem', 'rb').read()
				for com in range(len(resp)):
					ret.update({com: [Sec.encrypt_(str(value), pub) for value in resp[com]]})
				return ret, 200
			else:
				return {'status': 'brak danych'}, 204
		except Exception:
			return {'status': 'wystapil blad'}, 500
