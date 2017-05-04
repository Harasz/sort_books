from flask import Flask, request
from flask_restful import Resource
from sort_api import Sec


class API_publicKey(Resource):

	def get(self):
		
		try:
			return {'publicKey': Sec.get_public()}, 200
		except:
			return {'status': 'blad'}, 500
