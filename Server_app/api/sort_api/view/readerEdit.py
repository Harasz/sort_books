from flask import Flask, request
from flask_restful import Resource
from sort_api import cur, auth_k, parser, Sec


class API_readerEdit(Resource):

	def post(self):
		
		data = Sec.encode_data(parser.parse_args())	
		
		if not data['key'] in auth_k:
			return {'status': 'brak autoryzacji'}, 401
		
		#try:
		cur.execute("""UPDATE librarians.readers
						SET name=%s, addres=%s 
						WHERE id_r=%s;""", (data['arg1'], data['arg2'], data['name_id'] ))
		return {'status': 'zmieniono'}, 200
		#except Exception as e:
		#	return {'status': Sec.encrypt_(str(e), open('pem/'+data['key']+'.pem', 'rb').read())}, 500

