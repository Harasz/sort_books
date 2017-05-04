from flask import Flask, request
from flask_restful import Resource
from sort_api import cur, auth_k, parser, Sec


class API_addBook(Resource):
			
	def post(self):
		
		data = Sec.encode_data(parser.parse_args())
		
		if not data['key'] in auth_k:
			return {'status': 'brak autoryzacji'}, 401
		
		try:
			cur.execute("SELECT * FROM librarians.books WHERE title=%s AND author=%s;", (data['arg1'], data['arg2']))
			resp = cur.fetchone()
			if resp:
				cur.execute("UPDATE librarians.books SET count=%s WHERE id_b=%s;", (data['book_id']+resp[3], resp[0]))
				return {'status': 'istnieje/dodano'}, 507
			else:
				cur.execute("INSERT INTO librarians.books (title, author, count) VALUES (%s, %s, %s);", (data['arg1'], data['arg2'], data['book_id']))
				return {'status': 'dodano'}, 201
		except Exception as e:
			return {'status': Sec.encrypt_(e, open('pem/'+data['key']+'.pem', 'rb').read())}, 500

