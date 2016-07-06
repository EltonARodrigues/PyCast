# -*- coding: utf-8 -*-

from XMLCSV.XMLdata import XMLdata
from XMLCSV.csv_import import CSVfeed
import os
import csv

if __name__ == '__main__':

    os.system('clear')
    id_p = 'continue'
    while id_p == 'continue':

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
            cont_p = CSV.select()
            if cont_p != -1:
                
                id_p = input("\nType it ID or new/remove feed: ")
                if type(id_p) is str:
                    id_p = id_p.lower()

            if id_p == 'remove':
                id_remove = input("Insert ID to remove feed: ")
                CSV.remove(id_remove)
                id_p = 'continue'
                os.system('clear')

            elif id_p == 'new':

                url = input("Insert Feed URL: ")

                if CSV.verify(url) is True:
                    os.system('clear')
                    print('\t\t\t\t\tFeed already added')

                elif AttributeError is True:
                    os.system('clear')
                    print("\t\t\t\t\tfeed link invalid")

                else:
                    XMLdata(url).add_feed()
                id_p = 'continue'
            else:

                url = CSV.get_url(id_p)
            
        except IndexError:

            os.system('clear')
            print("\t\t\t\t\tID not found")

    

    while 1:
        print('Loading...')
        m = XMLdata(url)
        search = input('Episode name: ')
        search = str.title(search)

        mp3, name_mp3, error_search = m.search_pod(m.feed_in(), search)

        if error_search != 1:
            break

        os.system('clear')
        print('\t\t\t\t\tEpisode not found!')

    dow = input("Want to Do Download this podcast ( Yes / No) : ")
    dow = str.upper(dow)

    if dow == "YES":

        print("Downloading..... ")

        podcast_name = m.title_p
        m.download(name_mp3, m.clear_link(mp3), podcast_name)

    print("Exiting....")
