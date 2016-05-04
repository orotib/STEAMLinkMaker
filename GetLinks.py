#!/usr/bin/env python
#encoding: utf-8

import datetime
import json
import os
import random
import sys
import time

from bs4 import BeautifulSoup
import pyperclip
import requests

"""
<tr> elemek kigyűjése a 'filename' nevű állományból, ami egy szöveges fájl (a weblap html kódja lementve)
"""
def get_tr_elements(filename):
	#html = open(filename, 'r').read()
	#s = requests.Session()
	#html = s.get(filename)
	html = requests.get(filename)
	parsered_text = BeautifulSoup(html.content, 'html.parser')
	data = parsered_text.find_all('tr')
	#Az elso elem nem fegyverleírást tartalmaz
	del data[0]
	return data

"""
A 'get_tr_elements' által visszaadott adathalmazból kigyűjtjük a nekünk kellő infókat és a 'filename'-be kiírjuk
weapon - fegyvernév (pl.: Tec-9, AK-47)
skin - skin neve (pl.: Redline, Asiimov)
"""
def print_to_file(data, filename):
	out = open(filename, 'w')
	for elem in data:
		tds = elem.find_all('td')
		weapon = tds[1].text.encode('utf-8').strip().replace(' ', '%20')
		skin = tds[2].text.encode('utf-8').strip().replace(' ', '%20').replace('*','')
		out.write(weapon+ ';' + skin + '\n')
	out.close()


####################################################################################################################
data = get_tr_elements('http://counterstrike.wikia.com/wiki/Skins/List')
print_to_file(data, 'out')
