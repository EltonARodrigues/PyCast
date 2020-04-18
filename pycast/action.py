# -*- coding: UTF-8 -*-

from .feed import Feed
from .rss import RSS
from .opml import OPML
import os
import sys

feed = Feed()


class Action_add:

    def __init__(self, next_action):
        self.__next_action = next_action

    def command(self, action):
        if action == 'new':

            action = input('\nOptions:\n-Enter the Feed or the .opml directory'
                           '\n-Type (home) to return\n$ ')

            if str.find(action, "opml") > 0:

                print('Loading...')
                OPML(action).get()
            else:
                if str.find(action, "https://") != 0:

                    if str.find(action, "http://") != 0:
                        action = "http://" + action

                print("Loading...")
                print(action)
                RSS(action).new()
        else:
            return self.__next_action.command(action)


class Action_remove:

    def __init__(self, next_action):
        self.__next_action = next_action

    def command(self, action):
        if action == 'remove':
            remove_input = input('\nOptions:\n-Insert ID to remove'
                                 '\n-Type (all) to remove all'
                                 '\n-Type (home) to return\n$ ')

            if remove_input == 'all':
                feed.remove_all()

            elif remove_input == 'home':
                pass

            else:
                feed.remove(remove_input)
        else:
            return self.__next_action.command(action)


class Action_id:

    def __init__(self, next_action):
        self.__next_action = next_action

    def command(self, action):
        if action.isdigit():
            return feed.url(action)

        else:
            return self.__next_action.command(action)


class Action_exit:

    def __init__(self, next_action):
        self.__next_action = next_action

    def command(self, action):
        if action == 'exit':
            sys.exit()

        else:
            return self.__next_action.command(action)


class No_action:

    def command(self, action):
        return True
