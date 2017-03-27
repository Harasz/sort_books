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
import random

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('login', type=str)
parser.add_argument('pass_', type=str)
parser.add_argument('name', type=str)
parser.add_argument('address', type=str)


class Sort_Books_webApi(Resource):
			
	def post(self):
		data = parser.parse_args()
		
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
		
		#if not data['key'] in auth_k:
		#	return {'status': 'brak autoryzacji'}, 401
		
		#try:
		cur.execute("SELECT * FROM librarians.readers WHERE name='%s' AND addres='%s';" % (data['name'], data['address']))
		resp = cur.fetchall()
		if resp:
			return {'status': 'istnieje'}, 507
		else:
			cur.execute("SELECT * FROM librarians.readers")
			resp = cur.fetchall()
			print(len(resp))
			cur.execute("INSERT INTO librarians.readers VALUES ("+str(len(resp))+", '%s', '%s');" % (data['name'], data['address']))
			return {'status': 'dodano'}, 201
		#except:
		#	return {'status': 'blad'}, 500



api.add_resource(Sort_Books_webApi, '/api/logaction')
api.add_resource(Sort_Books_addRe, '/api/addre')

if __name__ == '__main__':
	
	auth_key = []
	with psycopg2.connect(dbname='librarians', user='postgres', host='192.168.0.99', password='dsp2017') as conn:
		try:
			cur = conn.cursor()
			app.run(host='0.0.0.0', debug=True)
		except:
			print('[Error] Wystapil blad')
			exit()