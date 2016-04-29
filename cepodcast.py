#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
from subprocess import call
import sys
import requests
import random
import urllib.request
import shutil

page=requests.get('http://www.powerfm.com.tr/podcasts/2016/cenk-erdem.html')
tree=html.fromstring(page.content)

songs = tree.xpath('//div[@class="podcastPlay"]/span/text()')

while True:
	song = random.choice(songs)
	print(song)
	#file_name, headers = urllib.request.urlretrieve(song)
	file_name=song.split('/')[-1]
	with urllib.request.urlopen(song) as response, open(file_name, 'wb') as out_file:
		shutil.copyfileobj(response, out_file)
	print(file_name)
	try:
		call(["mplayer", file_name])
	except:
		print('mplayer çalıştırılamadı !!!')
	print('x:Çıkış')
	c = sys.stdin.read(1)
	if c == 'x':
		break


