from flask import render_template, Blueprint, session, redirect, url_for, request
from sort_books import cur
import datetime

book_blueprint = Blueprint('book_blueprint', __name__)


@book_blueprint.route('/books')
def avalibe():
	cur.execute("SELECT * FROM librarians.books WHERE id_b>0;")
	resp = cur.fetchall()
	return render_template('books.html', books=resp)


@book_blueprint.route('/book/id/<int:id_book>', methods=['POST', 'GET'])
def book_info(id_book):
	allow_com = False
	if 'auth' in session:
		cur.execute("SELECT id_br FROM librarians.borrows WHERE book_id=%s AND name_id=%s;", (id_book, session['auth']['id']))
		if cur.fetchone():
			allow_com = True

	if request.method == 'GET':
		cur.execute("SELECT * FROM librarians.comments WHERE id_b =%s;", (id_book, ))
		comments = cur.fetchall()
		cur.execute("SELECT * FROM librarians.books WHERE id_b=%s;", (id_book, ))
		resp = cur.fetchone()
		if resp[3]==1:
			item = 'Dostępny jeden egzemplarz'
		elif resp[3]>0:
			item = 'Dostępnych '+str(resp[3])+' egzemplarzy'
		else:
			cur.execute("SELECT return FROM librarians.borrows WHERE book_id=%s AND give_back='false' ORDER BY return;", (id_book, ))
			ret = cur.fetchall()
			item = 'Książka będzie dostępna najwcześniej w '+ret[0][0].isoformat()
		return render_template('book.html', book=resp, item=item, allow_com=allow_com, comments=comments)
	else:
		if not 'auth' in session or not allow_com:
			return redirect(url_for('book_blueprint.book_info', id_book=id_book))
		
		cur.execute("SELECT id_comment FROM librarians.comments;")
		cur.execute("INSERT INTO librarians.comments VALUES ("+str(len(cur.fetchall()))+", %s, %s, %s, %s);", (id_book, request.form['comment'], datetime.datetime.now().strftime('%d-%m-%y'), session['auth']['username']))
		return redirect(url_for('book_blueprint.book_info', id_book=id_book))
