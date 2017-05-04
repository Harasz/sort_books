from flask import Flask, request
from flask_restful import Resource
from sort_api import cur, auth_k, parser, Sec


class API_addBorrow(Resource):
			
	def post(self):
		
		data = Sec.encode_data(parser.parse_args())
		
		if not data['key'] in auth_k:
			return {'status': 'brak autoryzacji'}, 401
		
		try:
			cur.execute("SELECT give_back FROM librarians.borrows WHERE name_id=%s AND book_id=%s AND give_back='0';", (data['name_id'], data['book_id']))
			resp = cur.fetchall()
			if resp:
				return {'status': 'istnieje'}, 507
			else:
				cur.execute("""
				INSERT INTO librarians.borrows VALUES (default, %s, %s, %s, %s, '0');
				UPDATE librarians.books SET count=count-1 WHERE id_b=%s;
				""", (data['arg1'], data['arg2'], data['name_id'], data['book_id'], data['book_id']))
				return {'status': 'dodano'}, 201
		except Exception as e:
			return {'status': Sec.encrypt_(e, open('pem/'+data['key']+'.pem', 'rb').read())}, 500

