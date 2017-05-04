#!flask/bin/python
from flask import Flask, session
from sort_books import views, app


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001, debug=True)
