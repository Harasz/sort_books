from flask import render_template, Blueprint, session, redirect, url_for, request
from sort_books import cur, login_required
from hashlib import sha512


login_blueprint = Blueprint('login_blueprint', __name__)


@login_blueprint.route('/login', methods=['POST', 'GET'])
def auth_in():
	if 'auth' in session:
		return redirect(url_for('index_blueprint.index'))
		
	error = None
	class LoginError(Exception):pass
	
	try:
		if request.method == 'POST' and not 'auth' in session:
			resp = auth(request.form['username'], sha512(request.form['password'].encode('UTF-8')).hexdigest())
			if resp:
				session['auth'] = {'id': resp[0], 'username': resp[1], 'address': resp[2], 'email': resp[3], 'login': resp[6]}
				if not resp[5]:
					session['auth']['adj'] = True
					return redirect(url_for('login_blueprint.auth_adjust'))
				else:
					return redirect(url_for('index_blueprint.index', l=True))
			else:
				raise LoginError('Błędne dane logowania!')
	except LoginError as fail:
		error=fail
	return render_template('login.html', error=error)


@login_blueprint.route('/logout')
@login_required
def auth_out():
	session.pop('auth', None)
	return redirect(url_for('login_blueprint.auth_in'))

@login_blueprint.route('/acc/adjust',  methods=['POST', 'GET'])
@login_required
def auth_adjust():
	if session['auth']['adj']:
		if request.method == 'POST':
			if 'email' in request.form:
				if request.form['email'] == request.form['email2']:
					cur.execute("UPDATE librarians.readers SET email=%s WHERE id_r=%s;", (request.form['email'], session['auth']['id']))
					session['auth']['email'] = request.form['email']
					return render_template('adj.html', step=2)
				else:
					return render_template('adj.html', step=1, error="Podane adresy email nie są identyczne")
			elif 'pass' in request.form:
				if request.form['pass'] == request.form['pass2']:
					cur.execute("UPDATE librarians.readers SET pass=%s WHERE id_r=%s;", (sha512(request.form['pass'].encode('UTF-8')).hexdigest(), session['auth']['id']))
					return render_template('adj.html', step=3)
				else:
					return render_template('adj.html', step=2, error="Podane hasła nie są identyczne")
			else:
				if request.form.getlist('allow_email'): allow_email = 'true'
				else: allow_email = 'false'
				if request.form.getlist('allow_address'): allow_address = 'true'
				else: allow_address = 'false'
				if request.form.getlist('allow_profile'): allow_profile = 'true'
				else: allow_profile = 'false'
				
				cur.execute("INSERT INTO librarians.readers_pref VALUES (%s, %s, %s, %s);", (session['auth']['id'], allow_email, allow_address, allow_profile))
				cur.execute("UPDATE librarians.readers SET loged=true WHERE id_r=%s;", (session['auth']['id'], ))
				return render_template('adj.html', step=4)
		else:
			return render_template('adj.html', step=1)
	else:
		return redirect(url_for('index_blueprint.index'))


def auth(login, pas):
	cur.execute("SELECT * FROM librarians.readers WHERE login=%s OR email=%s AND pass=%s;", (login, login, pas))
	return cur.fetchone()
