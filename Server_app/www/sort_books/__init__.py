#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  __init__.py
#  
#  Copyright 2017 root <root@lap>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from flask import Flask, session, redirect, url_for
from flask_recaptcha import ReCaptcha
from random import sample
from configparser import ConfigParser
from functools import wraps
from smtpConf import SMTP_conn
from ast import literal_eval
import psycopg2


app = Flask(__name__)
app.secret_key = ''.join(sample('qwertyuiopasdfgjhklzxcvbnm1234567890', 10))


conf = ConfigParser()
conf.read(filenames='./server.cfg')

app.config.update({
	"RECAPTCHA_SITE_KEY": conf['RECAPTCHA']['Site_Key'],
	"RECAPTCHA_SITE_SECRET": conf['RECAPTCHA']['Secret_Key'],
	"RECAPTCHA_ENABLED": literal_eval(conf['RECAPTCHA']['Enabled']),
})

recaptcha = ReCaptcha()
recaptcha.init_app(app)

try:
	conn = psycopg2.connect(dbname=conf['SERVER_SQL']['Database'],
							user=conf['SERVER_SQL']['User'],
							host=conf['SERVER_SQL']['Address'],
							password=conf['SERVER_SQL']['Password'])
	conn.autocommit = True
	cur = conn.cursor()
except Exception as e:
	print("[Error] Wystapił bład z bazą danych:\n"+str(e))
	exit()


try:
	smtp = SMTP_conn(address = conf['SMTP']['Address'],
					port = conf['SMTP']['Port'],
					login = conf['SMTP']['E-mail'],
					password = conf['SMTP']['Password'])
except Exception as e:
	print("[Error] Wystapił bład z serwerem SMTP:\n"+str(e))
	exit()
	

def login_required(func):
	@wraps(func)
	def check(*args, **kwargs):
		if 'auth' in session:
			return func(*args, **kwargs)
		return redirect(url_for('login_blueprint.auth_in'))
	return check


from sort_books import views, error_handler
