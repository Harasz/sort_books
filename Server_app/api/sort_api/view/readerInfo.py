from flask_restful import Resource
from sort_api import cur, login_required, parser, Sec


class API_readerInfo(Resource):

    def post(self):

        data = Sec.encode_data(parser.parse_args())

        if not login_required(data):
            return {'status': 'brak autoryzacji'}, 401

        try:
            cur.execute("SELECT * FROM librarians.readers WHERE id_r=%s;", (data['arg1'], ))
            resp = cur.fetchone()
            if resp:
                pub = open('pem/'+data['key']+'.pem', 'rb').read()
                return {'data': [Sec.encrypt_(str(value), pub) for value in resp]}, 200
            else:
                return {'status': 'brak danych'}, 204
        except Exception:
            return {'status': 'wystapil blad'}, 500
