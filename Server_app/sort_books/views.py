from flask import render_template, Blueprint, session, url_for, redirect
from .blueprints.index import index_blueprint
from .blueprints.login import login_blueprint
from .blueprints.acc import acc_blueprint
from .blueprints.books import book_blueprint
from .blueprints.mybook import mybook_blueprint
from .blueprints.rank import rank_blueprint
from sort_books import app


app.register_blueprint(index_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(acc_blueprint)
app.register_blueprint(book_blueprint)
app.register_blueprint(mybook_blueprint)
app.register_blueprint(rank_blueprint)


@app.template_filter('split_space')
def split_space(s):
	return s.split(' ')[0]
