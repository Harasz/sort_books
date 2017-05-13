from flask import Flask, request
from flask_restful import Resource
from sort_api import cur, login_required, parser, Sec, auth_k


class API_librariansEdit(Resource):

	def post(self):

		data = Sec.encode_data(parser.parse_args())	

		if not login_required(data):
			return {'status': 'brak autoryzacji'}, 401
		
		accept = False
		for key in auth_k:
			if key[0] == data['key']:
				accept = str(key[1])
				break
		
		if accept==False:
			return {'status': 'brak autoryzacji'}, 401

		try:
			cur.execute("SELECT master FROM librarians.user WHERE id=%s ORDER BY id ASC;", (accept, ))
			resp = cur.fetchone()
			if resp:
				if data['arg3'] == 'True': data['arg3'] = '1'
				else: data['arg3'] = '0'
				cur.execute("""UPDATE librarians.user
							SET imie=%s, nazwisko=%s, email=%s, master=%s 
							WHERE id=%s;""", (data['arg1'], data['arg2'], data['login'], data['arg3'], data['name_id']))
						
				return {'status': 'zmieniono'}, 200
			else:
				return {'status': 'brak autoryzacji'}, 401
		except Exception:
			return {'status': 'wystapil blad'}, 500
