from flask_restful import Resource
from sort_api import cur, login_required, parser, Sec


class API_getBorrows(Resource):

    def post(self):

        data = Sec.encode_data(parser.parse_args())

        if not login_required(data):
            return {'status': 'brak autoryzacji'}, 401

        try:
            cur.execute("""
            SELECT bor.rented, re.name, bo.title, bor.give_back, bor.id_br
            FROM librarians.borrows AS bor, librarians.books AS bo, librarians.readers AS re
            WHERE bor.name_id=re.id_r AND bor.book_id=bo.id_b
            ORDER BY bor.id_br ASC;
            """)

            resp = cur.fetchall()
            if resp:
                ret = {}
                pub = open('pem/'+data['key']+'.pem', 'rb').read()
                for borrow in range(len(resp)):
                    cache = (resp[borrow][0].isoformat(), resp[borrow][1], resp[borrow][2],
                             resp[borrow][3], resp[borrow][4])
                    ret.update({borrow: [Sec.encrypt_(str(value), pub) for value in cache]})
                return ret, 200
            else:
                return {'status': 'brak danych'}, 204
        except Exception:
            return {'status': 'wystapil blad'}, 500
