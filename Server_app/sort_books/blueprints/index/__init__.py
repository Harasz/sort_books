from flask import render_template, Blueprint, session, redirect, url_for, request
import os, glob

index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.route('/')
def index():
	return  render_template('index.html', log=request.args.get('l'))
	
@index_blueprint.route('/contact')
def contact():
	return render_template('contact.html')

@index_blueprint.route('/galery')
def galery():
	path = glob.glob('sort_books/static/images/galery/*.png')
	for i in range(len(path)):
		path[i] = path[i][10:]
	print(path)
	return render_template('galery.html', image=path)
