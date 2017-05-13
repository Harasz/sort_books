from flask import Flask, request
from flask_restful import Resource
from sort_api import cur, login_required, parser, Sec
import datetime


class API_retBook(Resource):
			
	def post(self):
		
		data = Sec.encode_data(parser.parse_args())	
		
		if not login_required(data):
			return {'status': 'brak autoryzacji'}, 401
		
		try:
			cur.execute("SELECT * FROM librarians.borrows WHERE id_br=%s AND give_back='1';", (data['arg1'], ))
			resp = cur.fetchone()
			if resp:
				return {'status': 'istnieje'}, 507
			else:
				cur.execute("""
				UPDATE librarians.books SET count=count+1 WHERE id_b=(SELECT book_id FROM librarians.borrows WHERE id_br=%s AND give_back='0');
				UPDATE librarians.borrows SET return=%s, give_back='1' WHERE id_br=%s;
				""", (data['arg1'], datetime.datetime.now().strftime("%Y-%m-%d"), data['arg1']))
				return {'status': 'dodano'}, 201
		except Exception:
			return {'status': 'wystapil blad'}, 500
