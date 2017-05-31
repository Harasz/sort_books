from flask_restful import Resource
from sort_api import Sec


class API_publicKey(Resource):

    def get(self):

        try:
            return {'publicKey': Sec.get_public()}, 200
        except Exception:
            return {'status': 'wystapil blad'}, 500
