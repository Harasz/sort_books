#!flask/bin/python
from sort_books import views, app, conf


if __name__ == '__main__':
    app.run(host=conf['GENERAL']['Address'],
            port=int(conf['GENERAL']['Port']),
            debug=conf['GENERAL']['Debug'])
