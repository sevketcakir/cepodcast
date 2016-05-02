#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
from subprocess import call
import sys
import requests
import random
import os.path
from urllib.request import urlretrieve
import time

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %5.1fM / %5.1fM" % (percent, readsofar / 1048576.0, totalsize / 1048576.0)
        sys.stderr.write(s)
        if readsofar >= totalsize:  # near the end
            sys.stderr.write("\n")
    else:  # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))


plist = list()  # Tüm yıllardaki kayıtları tutacak liste
with open("podcastlist.txt") as f:
    for line in f:
        if line[0] != '#':
            page = requests.get(line)
            tree = html.fromstring(page.content)
            songs = tree.xpath('//div[@class="podcastPlay"]/span/text()')
            plist = plist + songs

print(len(plist), ' podcast mevcut...\n')

while True:
    song = random.choice(plist)
    print(song)
    file_name = 'sound/'+song.split('/')[-1]
    if not os.path.isfile(file_name):  # Dosya mevcut degilse
        try:
            urlretrieve(song, file_name, reporthook)
        except KeyboardInterrupt:
            print('\nÇıkılıyor...')
            hd = open('hatali.txt', "a")
            hd.write(file_name + '\n')
            hd.close()
            sys.exit()
        except:
            print('\nDosya indirmede hata!!')
            hd = open('hatali.txt', "a")
            hd.write(file_name + '\n')
            hd.close()

    print(file_name)
    try:
        call(["mplayer", file_name])
    except:
        print('mplayer çalıştırılamadı !!!')
    try:
        print('Çıkış için Ctrl+C tuşlarına basın...')
        time.sleep(5)
    except KeyboardInterrupt:
        print('Çıkılıyor...')
        sys.exit()
