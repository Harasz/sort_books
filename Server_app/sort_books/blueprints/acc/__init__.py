from flask import render_template, Blueprint, session, redirect, url_for, request, abort
from hashlib import sha512
from sort_books import cur

acc_blueprint = Blueprint('acc_blueprint', __name__)


@acc_blueprint.route('/acc/<int:user_id>')
def profile(user_id):
	cur.execute("SELECT * FROM librarians.readers WHERE id_r='%s' AND loged='true';" %(user_id))
	resp = cur.fetchone()
	if not resp==None:
		cur.execute("SELECT * FROM librarians.readers_pref WHERE reader_id = '%s';" %(user_id))
		pref = cur.fetchone()
		if not pref[3] and not 'auth' in session:
			return abort(404)
		else:
			cur.execute("SELECT * FROM librarians.borrows WHERE name_id='%s' AND give_back='true';" %(user_id))
			count = cur.fetchall()
			info = {'name': resp[1], 'book_count': len(count), 'email': 'ukryto', 'address': 'ukryto', 'owner': False}
			
			if pref[1] or 'auth' in session and user_id == session['auth']['id']: info['email'] = resp[3]
			if pref[2] or 'auth' in session and user_id == session['auth']['id']: info['address'] = resp[2]
		
			return render_template('profile.html', user=info)
	else:
		return abort(404)


@acc_blueprint.route('/acc/settings', methods=['POST', 'GET'])
def settings():
	if not 'auth' in session:
		return redirect(url_for('index_blueprint.index'))
	
	cur.execute("SELECT * FROM librarians.readers_pref WHERE reader_id = '%s';" %(session['auth']['id']))
	pref = cur.fetchone()
	
	if request.method == 'POST':
		if 'pass' in request.form:
			cur.execute("SELECT pass FROM librarians.readers WHERE id_r='%s';" % (session['auth']['id']))
			if sha512(request.form['old_pass'].encode('UTF-8')).hexdigest() == cur.fetchone()[0] and request.form['new_pass']==request.form['new_pass2']:
				cur.execute("UPDATE librarians.readers SET pass='%s' WHERE id_r = '%s';" %(sha512(request.form['new_pass'].encode('UTF-8')).hexdigest(),session['auth']['id']))
				return render_template('settings.html', pref=pref, update=True)
			else:
				return render_template('settings.html', pref=pref, update='Hasła się nie zgadzają')
		elif 'email' in request.form:
			cur.execute("UPDATE librarians.readers SET email='%s' WHERE id_r = '%s';" %(request.form['email'],session['auth']['id']))
			return render_template('settings.html', pref=pref, update=True)
		elif 'privacy' in request.form:
			if request.form.getlist('allow_email'): allow_email = 'true'
			else: allow_email = 'false'
			if request.form.getlist('allow_address'): allow_address = 'true'
			else: allow_address = 'false'
			if request.form.getlist('allow_profile'): allow_profile = 'true'
			else: allow_profile = 'false'
			cur.execute("UPDATE librarians.readers_pref SET allow_email='%s', allow_address='%s', allow_profile='%s' WHERE reader_id = '%s';" %(allow_email, allow_address, allow_profile, session['auth']['id']))
			return render_template('settings.html', pref=pref, update=True)
	else:
		return render_template('settings.html', pref=pref)
	
	
