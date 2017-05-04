from flask import Flask, request
from flask_restful import Resource
from sort_api import cur, auth_k, parser, Sec


class API_acceptCom(Resource):

	def post(self):
		
		data = Sec.encode_data(parser.parse_args())	
		
		if not data['key'] in auth_k:
			return {'status': 'brak autoryzacji'}, 401
		
		try:
			if data['arg2']=='True':
				cur.execute("UPDATE librarians.comments SET accept='1' WHERE id_comment=%s;", (data['arg1'], ))
				return {'status': 'zaakceptowano'}, 200
			else:
				cur.execute("DELETE FROM librarians.comments WHERE id_comment=%s;", (data['arg1'], ))
				return {'status': 'usunieto'}, 200
		except Exception as e:
			return {'status': Sec.encrypt_(e, open('pem/'+data['key']+'.pem', 'rb').read())}, 500
