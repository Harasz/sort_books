#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  run.py
#  
#  Copyright 2017 root <root@lap>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from hashlib import sha512
import psycopg2
import random, datetime

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('login', type=str)
parser.add_argument('pass_', type=str)
parser.add_argument('key', type=str)
parser.add_argument('arg1', type=str)
parser.add_argument('arg2', type=str)
parser.add_argument('book_id', type=int)
parser.add_argument('name_id', type=int)


class Sort_Books_webApi(Resource):
			
	def post(self):
		data = parser.parse_args()
		global auth_k
		
		try:
			pass_ = sha512(data['pass_'].encode('UTF-8')).hexdigest()
			cur.execute("SELECT * FROM librarians.user WHERE email='%s' AND haslo='%s';" % (data['login'], pass_))
			resp = cur.fetchall()
			if resp:
				cache = ''.join(random.sample('qwertyuiopasdfghjklzxcvbnm1234567890', 15))
				auth_k.append(cache)
				return {'auth': cache,'Imie': resp[0][1], 'Nazwisko': resp[0][2], 'Email': resp[0][3]}, 200
			else:
				return {'status': 'zle dane'}, 406
		except:
			return {'status': 'blad'}, 500

class Sort_Books_addRe(Resource):
			
	def post(self):
		data = parser.parse_args()
		global auth_k
		if not data['key'] in auth_k:
			return {'status': 'brak autoryzacji'}, 401
		
		print(data['arg1'], data['arg2'])
		try:
			cur.execute("SELECT * FROM librarians.readers WHERE name='%s' AND addres='%s';" % (data['arg1'], data['arg2']))
			resp = cur.fetchall()
			if resp:
				return {'status': 'istnieje'}, 507
			else:
				cur.execute("SELECT * FROM librarians.readers")
				resp = cur.fetchall()
				cur.execute("INSERT INTO librarians.readers VALUES ("+str(len(resp))+", '%s', '%s');" % (data['arg1'], data['arg2']))
				return {'status': 'dodano'}, 201
		except:
			return {'status': 'blad'}, 500


class Sort_Books_addBook(Resource):
			
	def post(self):
		data = parser.parse_args()
		global auth_k
		
		if not data['key'] in auth_k:
			return {'status': 'brak autoryzacji'}, 401
		
		try:
			cur.execute("SELECT * FROM librarians.books WHERE title='%s' AND author='%s';" % (data['arg1'], data['arg2']))
			resp = cur.fetchone()
			if resp:
				cur.execute("UPDATE librarians.books SET count='%s' WHERE id_b='%s';" % (data['book_id']+resp[3], resp[0]))
				return {'status': 'istnieje/dodano'}, 507
			else:
				cur.execute("SELECT * FROM librarians.books")
				resp = cur.fetchall()
				cur.execute("INSERT INTO librarians.books VALUES ( "+str(len(resp))+", '"+data['arg1']+"', '"+data['arg2']+"');")
				return {'status': 'dodano'}, 201
		except:
			return {'status': 'blad'}, 500
		
class Sort_Books_getReaders(Resource):
			
	def post(self):
		data = parser.parse_args()
		global auth_k
		
		if not data['key'] in auth_k:
			return {'status': 'brak autoryzacji'}, 401
		
		try:
			cur.execute("SELECT * FROM librarians.readers WHERE id_r>0;")
			resp = cur.fetchall()
			if resp:
				ret = {}
				for reader in range(len(resp)):
					ret.update({reader+1: resp[reader]})
				return ret, 200
			else:
				return {'status': 'brak danych'}, 204
		except:
			return {'status': 'blad'}, 500

class Sort_Books_getBooks(Resource):
			
	def post(self):
		data = parser.parse_args()
		global auth_k
		
		if not data['key'] in auth_k:
			return {'status': 'brak autoryzacji'}, 401
		
		try:
			cur.execute("SELECT * FROM librarians.books WHERE id_b>0;")
			resp = cur.fetchall()
			if resp:
				ret = {}
				for reader in range(len(resp)):
					ret.update({reader+1: resp[reader]})
				return ret, 200
			else:
				return {'status': 'brak danych'}, 204
		except:
			return {'status': 'blad'}, 500
			

class Sort_Books_getBorrows(Resource):
			
	def post(self):
		data = parser.parse_args()
		global auth_k
		
		if not data['key'] in auth_k:
			return {'status': 'brak autoryzacji'}, 401
		
		try:
			cur.execute("SELECT rented, name_id, book_id, give_back, id_br FROM librarians.borrows WHERE id_br>0;")
			resp = cur.fetchall()
			if resp:
				ret = {}
				for borrow in range(len(resp)):
					ret.update({borrow: (resp[borrow][0].isoformat(), resp[borrow][1], resp[borrow][2], resp[borrow][3], resp[borrow][4])})
				return ret, 200
			else:
				return {'status': 'brak danych'}, 204
		except:
			return {'status': 'blad'}, 500




class Sort_Books_addBorrow(Resource):
			
	def post(self):
		data = parser.parse_args()
		global auth_k
		
		if not data['key'] in auth_k:
			return {'status': 'brak autoryzacji'}, 401
		
		try:
			cur.execute("SELECT give_back FROM librarians.borrows WHERE name_id='%s' AND book_id='%s' AND give_back='0';" % (data['name_id'], data['book_id']))
			resp = cur.fetchall()
			if resp:
				return {'status': 'istnieje'}, 507
			else:
				cur.execute("SELECT * FROM librarians.borrows")
				resp = cur.fetchall()
				cur.execute("INSERT INTO librarians.borrows VALUES ("+str(len(resp)+1)+", '%s', '%s', '%s', '%s', '0');" % (data['arg1'], data['arg2'], data['name_id'], data['book_id']))
				cur.execute("UPDATE librarians.books SET count=count-1 WHERE id_b='%s';" % (data['book_id']))
				return {'status': 'dodano'}, 201
		except:
			return {'status': 'blad'}, 500


class Sort_Books_retBook(Resource):
			
	def post(self):
		data = parser.parse_args()		
		global auth_k
		
		if not data['key'] in auth_k:
			return {'status': 'brak autoryzacji'}, 401
		
		#try:
		cur.execute("SELECT * FROM librarians.borrows WHERE id_br='%s' AND give_back='1';" % (data['arg1']))
		resp = cur.fetchone()
		if resp:
			return {'status': 'istnieje'}, 507
		else:
			cur.execute("SELECT * FROM librarians.borrows WHERE id_br='%s' AND give_back='0';" % (data['arg1']))
			resp = cur.fetchone()
			cur.execute("UPDATE librarians.books SET count=count+1 WHERE id_b='%s';" % (resp[4]))
			cur.execute("UPDATE librarians.borrows SET give_back='1' WHERE id_br='%s';" % (data['arg1']))
			return {'status': 'dodano'}, 201
		#except:
		#	return {'status': 'blad'}, 500


api.add_resource(Sort_Books_webApi, '/api/logaction')
api.add_resource(Sort_Books_addRe, '/api/addre')
api.add_resource(Sort_Books_addBook, '/api/addbook')
api.add_resource(Sort_Books_getReaders, '/api/getreader')
api.add_resource(Sort_Books_getBooks, '/api/getbook')
api.add_resource(Sort_Books_addBorrow, '/api/borrow')
api.add_resource(Sort_Books_getBorrows, '/api/getborrow')
api.add_resource(Sort_Books_retBook, '/api/retbook')

if __name__ == '__main__':
	
	auth_k = []
	with psycopg2.connect(dbname='librarians', user='postgres', host='192.168.0.99', password='dsp2017') as conn:
		try:
			conn.autocommit = True
			cur = conn.cursor()
			app.run(host='0.0.0.0', debug=True)
		except:
			print('[Error] Wystapil blad')
			exit()
