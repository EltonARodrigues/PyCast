#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from .feed import Feed
from .rss import RSS

from xml.etree import ElementTree


class OPML():

    def __init__(self, file):
        self.__file = file

    def get(self):
        feed = Feed()
        self.__file = self.__file.replace("'", '')
        self.__file = self.__file.replace(' ', '')
        with open(self.__file, 'rt') as f:
            tree = ElementTree.parse(f)

        for node in tree.findall('.//outline'):
            url = node.attrib.get('xmlUrl')
            if url:
                try:
                    RSS(url).add()
                except (AttributeError):
                    pass
