from flask import render_template, Blueprint, session, redirect, url_for, request
from sort_books import cur, login_required, smtp, conf
from hashlib import sha512
from random import sample, choice
from ast import literal_eval
from requests import get
import json


class reCaptcha(object):
	
	site_key = conf['RECAPTCHA']['Site_Key']
	private_key = conf['RECAPTCHA']['Secret_Key']
	enable = literal_eval(conf['RECAPTCHA']['Enabled'])
	google_api = 'https://www.google.com/recaptcha/api/siteverify'
	
	def getSiteKey(self):
		if self.enable:
			return self.site_key
		else:
			return False
	
	def verify(self):
		if self.enable:
			resp = get(self.google_api,
					   params = {
								'secret': self.private_key,
								'response': request.form['g-recaptcha-response'],
								'remoteip': request.environ['REMOTE_ADDR']
								}
					   )
			return json.loads(resp.text)['success']
		else: return True


login_blueprint = Blueprint('login_blueprint', __name__)
pass_code = []
captcha = reCaptcha()


@login_blueprint.route('/login', methods=['POST', 'GET'])
def auth_in():
	if 'auth' in session:
		return redirect(url_for('index_blueprint.index'))
		
	error = None
	class LoginError(Exception):pass
	
	try:
		if request.method == 'POST' and not 'auth' in session:
			if not captcha.verify():
				raise LoginError("Captcha nie jest poprawna")
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
	return render_template('login.html', error=error, site_key=captcha.getSiteKey())


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
					cur.execute("SELECT * FROM librarians.readers WHERE email=%s;", (request.form['email'], ))
					if not cur.fetchone():
						cur.execute("UPDATE librarians.readers SET email=%s WHERE id_r=%s;", (request.form['email'], session['auth']['id']))
						session['auth']['email'] = request.form['email']
						return render_template('adj.html', step=2)
					else:
						return render_template('adj.html', error="Podany adres email jest już w użyciu", step=1) 
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
				text = open("email/NewUserEmail.txt").read()
				smtp.sendEmail(session['auth']['email'], 'Sort Books - Witamy!',
							   text.format(name=session['auth']['username']))
				return render_template('adj.html', step=4)
		else:
			return render_template('adj.html', step=1)
	else:
		return redirect(url_for('index_blueprint.index'))


@login_blueprint.route('/login/remind',  methods=['POST', 'GET'])
def remind():
	if request.method == 'POST':
		if 'email' in request.form:
			cur.execute("SELECT id_r FROM librarians.readers WHERE email=%s;", (request.form['email'], ))
			resp = cur.fetchone()
			if resp:
				code = ''.join(sample('qwertyuiopasdfghjklzxcvbnm1234567890', 32))
				pass_code.append((code, resp[0]))
				text = open("email/RemindPass.txt").read()
				smtp.sendEmail(request.form['email'], 'Sort Books - Przypomnienie hasła',
							   text.format(url=request.url+'?key='+code))
				return render_template('remind.html', step=2)
			else:
				return render_template('remind.html', step=1, error="Żadne konto nie jest przypisane do tego adresu email")
		elif 'key' in request.form:
			if request.form['pass'] == request.form['pass2']:
				index = [x for x in pass_code if x[0]==request.form['key']][0]
				pass_code.remove(index)
				cur.execute("UPDATE librarians.readers SET pass=%s WHERE id_r=%s;", 
							(sha512(request.form['pass'].encode('UTF-8')).hexdigest(), index[1]))
				return render_template('remind.html', step=4)
			else:
				return render_template('remind.html', step=3, key=request.form['key'], error="Hasła nie są identyczne")
		else:
			return render_template('remind.html', step=1, error="Wystąpił błąd w zapytaniu")
	else:
		if request.args.get("key"):
			try:
				if request.args.get("key") == [x[0] for x in pass_code][0]:
					return render_template('remind.html', step=3, key=request.args.get("key"))
			except IndexError:
				pass
			return render_template('remind.html', step=1, error="Wystąpił błąd w zapytaniu")
		else:
			return render_template('remind.html', step=1)


def auth(login, pas):
	cur.execute("SELECT * FROM librarians.readers WHERE (login=%s OR email=%s) AND pass=%s;", (login, login, pas))
	return cur.fetchone()
