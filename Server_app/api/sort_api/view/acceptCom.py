from flask_restful import Resource
from sort_api import cur, login_required, parser, Sec


class API_acceptCom(Resource):

    def post(self):

        data = Sec.encode_data(parser.parse_args())

        if not login_required(data):
            return {'status': 'brak autoryzacji'}, 401

        try:
            if data['arg2'] == 'True':
                cur.execute("UPDATE librarians.comments SET accept='1' WHERE id_comment=%s;", (data['arg1'], ))
                return {'status': 'zaakceptowano'}, 200
            else:
                cur.execute("DELETE FROM librarians.comments WHERE id_comment=%s;", (data['arg1'], ))
                return {'status': 'usunieto'}, 200
        except Exception:
            return {'status': 'wystapil blad'}, 500
