from subprocess import call
import glob
import random
import sys

songs = glob.glob('./*.mp3')
print(songs)
while True:
	song = random.choice(songs)
	print(song)
	try:
		call(['mplayer',song])
	except:
		print('mplayer calistirilamadi')
	print('x:Cikis')
	c = sys.stdin.read(1)
	if c == 'x':
		break
