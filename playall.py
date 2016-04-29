from subprocess import call
import glob
import random

songs = glob.glob('./*.mp3')
print(songs)
while True:
	song = random.choice(songs)
	print(song)
	try:
		call(['mplayer',song])
	except:
		print('mplayer calistirilamadi')
