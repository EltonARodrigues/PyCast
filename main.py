# -*- coding: utf-8 -*-
import feedparser
import urllib
import urllib.request
from modulos.modulos_main import Modulos
from dbc import DBconnect
import os 
#import pdb; pdb.set_trace()

if __name__ == '__main__':

    #ipdb.set_trace()a
    print("""
               ____        ______              __
              / __ \__  __/ ____/__  ___  ____/ /
             / /_/ / / / / /_  / _ \/ _ \/ __  /
            / ____/ /_/ / __/ /  __/  __/ /_/ /
           /_/    \__  /_/    \___/\___/\____/
                 /____/

            """)

    m = Modulos()
    db = DBconnect()

    id_p = 'n'
    while id_p == 'n':
        cont_p = db.select_feed()
        id_p = input("Type it ID or (n) for new feed: ")
        print(cont_p)
        if id_p == 'n' or id_p == 'N':

            url = input("Insert Feed URL: ")

            d = feedparser.parse(url)
            link_p = d.feed.title_detail.base
            title_p = d.feed.title_detail.value
            url_site =  d.feed.link
            db.insert_feed(title_p,url_site,link_p)
            os.system('clear')

        else:
            url = db.select_feedpod(id_p)


    search  = input ("Episode name: ")
    search = str.title(search)

    name_mp3, mp3 = m.pesquisa_pod(m.feed_in(url),search)
    print ("\n{}\n".format(name_mp3))

    dow = input("Want to Do Download this podcast ( Yes / No) : ")
    dow = str.upper(dow)

    if dow == "YES":

        print ("Downloading..... ")
        m.download(name_mp3,m.limpar_link(mp3))

    print("Exiting....")
