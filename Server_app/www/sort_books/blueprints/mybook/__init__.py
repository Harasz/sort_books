from flask import render_template, Blueprint, session, redirect, url_for, request
from sort_books import cur, login_required
import datetime

mybook_blueprint = Blueprint('mybook_blueprint', __name__)


@mybook_blueprint.route('/acc/mybook')
@login_required
def books():
	
	cur.execute("""
	SELECT bo.title, bor.rented, bor.return, bo.id_b, bor.give_back
	FROM librarians.borrows AS bor, librarians.books AS bo
	WHERE bor.name_id=%s AND bor.book_id=bo.id_b
	ORDER BY bor.id_br DESC;
	""", (session['auth']['id'], ))
	
	return render_template('mybook.html', bor=cur.fetchall())
