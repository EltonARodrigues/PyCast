#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import sqlite3
import os.path
import csv


class Feed:

    def __init__(self):
        self.__conn = sqlite3.connect('feed.db')
        self.__cur = self.__conn.cursor()

    def __del__(self):
        self.__conn.close()

    def search_for_db(self):
        pass

    def new(self, name, url):
        if not self.duplicated(url):
            self.__cur.execute('INSERT INTO feed(name, url) VALUES(?, ?)', (name, url))
            feed_id = self.__cur.lastrowid
            self.__conn.commit()
            return feed_id
        return False

    def number_of_podcasts(self):

        self.__cur.execute('SELECT id, name from feed')
        self.__conn.commit()

        podcasts_list = self.__cur.fetchall()

        list_of_podcasts_is_empty = lambda: len(podcasts_list) == 0

        if list_of_podcasts_is_empty():
            return False

        for podcast in podcasts_list:
            print('|\t{}\t{}\t'.format(podcast[0], podcast[1]))

    def duplicated(self, url):
        self.__cur.execute('SELECT EXISTS(SELECT url from feed where url= ? LIMIT 1)', (url, ))
        self.__conn.commit()
        return self.__cur.fetchone()[0]

    def url(self, podcast_id):

        try:
            self.__cur.execute('SELECT url from feed where id= ? LIMIT 1', (podcast_id, ))
            self.__conn.commit()
            return self.__cur.fetchone()[0]

        except TypeError:
            return False

    def remove(self, podcast_id):
        self.__cur.execute('DELETE FROM feed WHERE id = ?', (podcast_id, ))
        self.__conn.commit()

    def remove_all(self):
        self.__cur.execute('DELETE FROM feed')
        self.__conn.commit()
