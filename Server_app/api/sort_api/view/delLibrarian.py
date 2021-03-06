from flask_restful import Resource
from sort_api import cur, login_required, parser, Sec, auth_k


class API_delLibrarian(Resource):

    def post(self):

        data = Sec.encode_data(parser.parse_args())

        if not login_required(data):
            return {'status': 'brak autoryzacji'}, 401

        accept = False
        for key in auth_k:
            if key[0] == data['key']:
                accept = str(key[1])
                break

        if accept:
            return {'status': 'brak autoryzacji'}, 401

        try:
            cur.execute("SELECT master FROM librarians.user WHERE id=%s ORDER BY id ASC;", (accept, ))
            resp = cur.fetchone()
            if resp:
                cur.execute("DELETE FROM librarians.user WHERE id=%s;", (data['arg1'], ))

                return {'status': 'usunieto'}, 200
            else:
                return {'status': 'brak autoryzacji'}, 401
        except Exception:
            return {'status': 'wystapil blad'}, 500
