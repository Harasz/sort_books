#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  run.py
#  
#  Copyright 2017 Jakub Sydor
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

from sort_api import app, class_api
from configparser import ConfigParser
import glob
import os


def clear_pem():
	for pem_file in glob.glob('pem/*.pem'):
		os.remove(pem_file)


if __name__ == '__main__':
	
	clear_pem()
	class_api.Sort_Books_API()
	
	conf = ConfigParser()
	conf.read(filenames='server.cfg')
	
	app.run(host=conf['GENERAL']['Address'],
			port=int(conf['GENERAL']['Port']),
			debug=conf['GENERAL']['Debug'])
