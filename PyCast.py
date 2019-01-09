#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from pycast.action import Action_add, Action_exit, Action_id, Action_remove, No_action
from pycast.exception import IDError, LinkError
from pycast.feed import Feed
from pycast.opml import OPML
from pycast.rss import RSS
import validators
import os
import re


class Pycast:

    def __init__(self):
        self.command = True
        self.__alert = ''

    def menu(self):
        self.command = True
        while self.command:
            os.system('clear')
            print(F'Alert: {self.__alert}')
            print("""
     ____         ____          _
    |  _ \ _   _ / ___|__ _ ___| |_
    | |_) | | | | |   / _` / __| __|
    |  __/| |_| | |__| (_| \__ \ |_
    |_|    \__, |\____\__,_|___/\__|
            |___/
    """)
            print("\tID\tPodCast\t")
            print("-" * 39)

            feed = Feed()
            feed.search_file()

            try:
                if feed.number_of_podcasts() != -1:
                    self.command = input('\nType it ID or '
                                            'new/remove/exit feed: ').lower()
                else:
                    self.command = 'new'

                url = Action_add(
                    Action_remove(
                        Action_id(
                            Action_exit(
                                No_action())))).command(self.command)

                if self.verify_url(url):
                    self.__select_epsode(url)

            except TypeError:
                pass

            except IndexError:
                self.__alert = "ID not found"
                self.command = True

            except AttributeError:
                self.__alert = "Feed link invalid"
                self.command = True

    def __select_epsode(self, url):

        self.command = True
        while self.command:
            rss = RSS(url)
            search_input = input('\nOptions:'
                                 '\n-Search by name or leave blank to show all'
                                 '\n-Type (home) to return'
                                 '\nSearch: ')

            if search_input == 'home':
                self.command = False
                break

            else:
                mp3, mp3_name = rss.search_podcast(search_input)

                if mp3_name == 'home':
                    self.command = False
                    break

                else:
                    download = str.lower(input('Want to Do Download this podcast'
                                               '(yes/no): '))

                    if download == "yes":

                        print("Downloading.....")

                        rss.download(mp3_name, mp3)

                        self.command = True
                        self.__alert = F'Download Complete - {mp3_name}'
                        break
                    break

    def verify_url(self, url):
        re_url = re.compile("^(http:\/\/www\.|https:\/"
                                    "\/www\.|http:\/\/|https:\/\/)?"
                                    "[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\."
                                    "[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$")

        if re.match(re_url, url):
            self.command = True
            return True
        return False



if __name__ == '__main__':
    P = Pycast()
    while True:
        os.system('clear')
        P.menu()
