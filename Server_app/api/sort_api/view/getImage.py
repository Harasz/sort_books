from flask import Flask, request, send_file, abort
from flask_restful import Resource
import glob
import os


class API_getImage(Resource):

    def get(self):

        try:
            filename = glob.glob('sort_api/image/'+request.args.get('name')+'.*')
            if not filename: return abort(404)

            return send_file(os.getcwd()+'/'+filename[0],
                             mimetype='image/png')
        except Exception:
            return {'status': 'wystapil blad'}, 500

