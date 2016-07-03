# -*- coding: utf-8 -*-

from modulos.modulos_main import Modulos
from modulos.csv_import import CSVfeed
import os
import csv

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

        CSV = CSVfeed()
        CSV.file_csv()

        try:
            cont_p = CSV.select() #db.select_feed()
            if cont_p != -1:
                
                id_p = input("\nType it ID or (n) for new feed: ")
            else:
                id_p = 'n'

            if id_p == 'n' or id_p == 'N':

                url = input("Insert Feed URL: ")

                try:
                    if CSV.verify(url) == 0:
                        os.system('clear')
                        print('\t\t\t\t\tFeed already added')

                    else:

                        Modulos(url).add_feed()

                except AttributeError:

                    os.system('clear')
                    print("\t\t\t\t\tfeed link invalid")
            else:

                url = CSV.get_url(id_p)            #db.select_feedpod(id_p)

        except IndexError:

            os.system('clear')
            print("\t\t\t\t\tID not found")

    m = Modulos(url)

    while 1:

        search = input("Episode name: ")
        search = str.title(search)

        mp3, name_mp3, error_search = m.search_pod(m.feed_in(), search)

        if error_search != 1:
            break

        os.system('clear')
        print('\t\t\t\t\tEpisode not found!')

    print("\n{}\n".format(name_mp3)) #APAGAR LINHA 
    dow = input("Want to Do Download this podcast ( Yes / No) : ")
    dow = str.upper(dow)

    if dow == "YES":

        print("Downloading..... ")

        podcast_name = m.title_p
        m.download(name_mp3, m.clear_link(mp3), podcast_name)

    print("Exiting....")
