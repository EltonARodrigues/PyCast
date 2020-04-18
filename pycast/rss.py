#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from .feed import Feed
from urllib.request import Request
from urllib.request import urlopen
from operator import add
import feedparser
import os
import re


class RSS:

    def __init__(self, url):
        self.url = url
        self.__file = feedparser.parse(url)
        self.__episode = self.__file.feed.title_detail.base
        self.__episode_title = self.__file.feed.title_detail.value

    def new(self):
        return Feed().new(self.__episode_title, self.url)

    def __count_epsodios(self):
        print('Loading feed...')
        return self.__file, int((len(self.__file['entries'])))

    def download(self, name, url_mp3):
        req = Request(self.__clear_link(url_mp3),
                      headers={'User-Agent': 'Mozilla/5.0'})

        html = urlopen(req).read()

        name = add(name, '.mp3')

        # remove/filename
        if str.find(name, ','):
            name = name.replace('/', '')

        directory = add('PodCast/', self.__episode_title)
        directory = add(directory, '/')

        if not os.path.exists(directory):
            os.makedirs(directory)

        arq = open(add(directory, name), 'wb')
        arq.write(html)
        arq.close()

    def __clear_link(self, mp3):
        re_link = re.search('http.+mp3', mp3)
        return re_link.group(0)

    def search_podcast(self, search):
        d, epsode_numbers = self.__count_epsodios()
        list_q = {}
        quant_episodes = 0
        error_search = 0

        for i in range(epsode_numbers):
            titulo = (d['entries'][i]['title'])

            if str.find(str.upper(titulo), str.upper(search)) != -1:
                search_value = i
                list_q[int(quant_episodes)] = i
                quant_episodes += 1

                print(
                    "|{}|".format(i), "\t{}".format(
                        d['entries'][i]['title']))

        if quant_episodes > 1:
            while True:
                choice = input('options:\n-Type ID;'
                               '\n-Type "home" to return\n$ ')
                if choice == 'home':
                    return None, 'home'

                for quant in range(0, quant_episodes):
                    if str(list_q[quant]) == choice:
                        search_value = int(choice)
                        mp3 = str(d['entries'][search_value]['enclosures'])
                        name = str(d['entries'][search_value]['title'])
                        print("\n\n{}".format(name))
                        return mp3, name
