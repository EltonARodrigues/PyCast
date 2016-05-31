# -*- coding: utf-8 -*-

from modulos.modulos_main import Modulos
from modulos.dbc import DBconnect
import os

if __name__ == '__main__':

    os.system('clear')
    id_p = 'n'
    while id_p == 'n':

        print("""
                 ____         ____          _   
                |  _ \ _   _ / ___|__ _ ___| |_ 
                | |_) | | | | |   / _` / __| __|
                |  __/| |_| | |__| (_| \__ \ |_ 
                |_|    \__, |\____\__,_|___/\__|
                        |___/
                """)

        m = Modulos()
        db = DBconnect()

        try:

            cont_p = db.select_feed()
            if cont_p != -1:
                
                id_p = input("\nType it ID or (n) for new feed: ")
            else:
                id_p = 'n'

            if id_p == 'n' or id_p == 'N':

                url = input("Insert Feed URL: ")

                try:

                    if db.check_link_feed(url) == 0:
                        os.system('clear')
                        print('\t\t\t\t\tFeed already added')

                    else:

                        m.add_feed(url)

                except AttributeError:

                    os.system('clear')
                    print("\t\t\t\t\tfeed link invalid")
            else:

                url = db.select_feedpod(id_p)

        except IndexError:

            os.system('clear')
            print("\t\t\t\t\tID not found")

    while 1:

        search = input("Episode name: ")
        search = str.title(search)

        mp3, name_mp3, error_search = m.search_pod(m.feed_in(url), search)

        if error_search != 1:
            break

        os.system('clear')
        print('\t\t\t\t\tEpisode not found!')

    print("\n{}\n".format(name_mp3))
    dow = input("Want to Do Download this podcast ( Yes / No) : ")
    dow = str.upper(dow)

    if dow == "YES":

        print("Downloading..... ")

        nome_podcast = m.search_name_podcast(url)
        m.download(name_mp3, m.clear_link(mp3), nome_podcast)

    print("Exiting....")
