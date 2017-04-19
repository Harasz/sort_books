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
from random import sample
import psycopg2
from functools import wraps

app = Flask(__name__)
app.secret_key = ''.join(sample('qwertyuiopasdfgjhklzxcvbnm1234567890', 10))


conn = psycopg2.connect(dbname='librarians', user='postgres', host='192.168.0.108', password='dsp2017')
conn.autocommit = True
cur = conn.cursor()

def login_required(func):
	@wraps(func)
	def check(*args, **kwargs):
		if 'auth' in session:
			return func(*args, **kwargs)
		return redirect(url_for('login_blueprint.auth_in'))
	return check


from sort_books import views, error_handler
