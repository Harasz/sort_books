from flask_restful import Resource
from sort_api import cur, login_required, parser, Sec


class API_readerEdit(Resource):

    def post(self):

        data = Sec.encode_data(parser.parse_args())

        if not login_required(data):
            return {'status': 'brak autoryzacji'}, 401

        try:
            cur.execute("""UPDATE librarians.readers
                            SET name=%s, addres=%s 
                            WHERE id_r=%s;""", (data['arg1'], data['arg2'], data['name_id']))
            return {'status': 'zmieniono'}, 200
        except Exception:
            return {'status': 'wystapil blad'}, 5000

