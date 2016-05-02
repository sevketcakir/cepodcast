#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
from subprocess import call
import sys
import requests
import random
import os.path
from urllib.request import urlretrieve

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %5.1fM / %5.1fM" % (percent,  readsofar/1048576.0, totalsize/1048576.0)
        sys.stderr.write(s)
        if readsofar >= totalsize:  # near the end
            sys.stderr.write("\n")
    else:  # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))


page = requests.get('http://www.powerfm.com.tr/podcasts/2016/cenk-erdem.html')
tree = html.fromstring(page.content)

songs = tree.xpath('//div[@class="podcastPlay"]/span/text()')

while True:
    song = random.choice(songs)
    print(song)
    file_name = song.split('/')[-1]
    if not os.path.isfile(file_name):  # Dosya mevcut degilse
        try:
            urlretrieve(song, file_name, reporthook)
        except KeyboardInterrupt:
            print('\nÇıkılıyor...')
            hd = open('hatali.txt',"a")
            hd.write(file_name+'\n')
            hd.close()
            sys.exit()
        except:
            print('\nDosya indirmede hata!!')
            hd = open('hatali.txt',"a")
            hd.write(file_name+'\n')
            hd.close()

    print(file_name)
    try:
        call(["mplayer", file_name])
    except:
        print('mplayer çalıştırılamadı !!!')
        print('x:Cikis')
        c = sys.stdin.read(1)
        if c == 'x':
            break


