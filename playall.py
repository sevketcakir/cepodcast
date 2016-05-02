#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import call
import glob
import random
import sys
import time

songs = glob.glob('./*.mp3')
print(songs)
while True:
	song = random.choice(songs)
	print('Çalınan: '+song)
	try:
		call(['mplayer',song])
	except:
		print('mplayer calistirilamadi')
	print('Çıkış için Ctrl+C')
	try:
		time.sleep(5);
	except KeyboardInterrupt:
		print('\nÇıkılıyor...')
		sys.exit()
	#print('x:Cikis')
	#c = sys.stdin.read(1)
	#if c == 'x':
	#	break
