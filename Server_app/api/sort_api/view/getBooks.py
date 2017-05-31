from flask_restful import Resource
from sort_api import cur, login_required, parser, Sec


class API_getBooks(Resource):

    def post(self):

        data = Sec.encode_data(parser.parse_args())

        if not login_required(data):
            return {'status': 'brak autoryzacji'}, 401

        try:
            cur.execute("SELECT * FROM librarians.books ORDER BY id_b ASC;")
            resp = cur.fetchall()
            if resp:
                ret = {}
                pub = open('pem/'+data['key']+'.pem', 'rb').read()
                for reader in range(len(resp)):
                    ret.update({reader+1: [Sec.encrypt_(str(value), pub) for value in resp[reader]]})
                return ret, 200
            else:
                return {'status': 'brak danych'}, 204
        except Exception:
            return {'status': 'wystapil blad'}, 500
