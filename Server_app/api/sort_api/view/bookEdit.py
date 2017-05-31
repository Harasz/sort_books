from flask import Flask, request
from flask_restful import Resource
from sort_api import cur, login_required, parser, Sec
from werkzeug import secure_filename
import os

allow = set(['png', 'jpg', 'jpeg', 'gif'])


def check_ext(f):
    f = f.filename
    return '.' in f and \
        f.rsplit('.', 1)[1] in allow


class API_bookEdit(Resource):

    def post(self):

        data = Sec.encode_data(parser.parse_args())

        if not login_required(data):
            return {'status': 'brak autoryzacji'}, 401

        try:
            if 'cover' in request.files and check_ext(request.files['cover']):
                f = request.files['cover']
                cover = secure_filename(data['arg1'])
                f.save(
                        os.path.join('sort_api/image/'+cover+'.'+f.filename.split('.')[1])
                      )

            cur.execute("""UPDATE librarians.books
                            SET title=%s, author=%s, count=%s 
                            WHERE id_b=%s;""", (data['arg1'], data['arg2'], data['arg3'], data['book_id']))

            return {'status': 'zmieniono'}, 200
        except Exception:
            return {'status': 'wystapil blad'}, 500
