# -*- coding: utf-8 -*-
import feedparser
import urllib
import urllib.request
from modulos.modulos_main import Modulos
from dbc import DBconnect
import os 
import time

if __name__ == '__main__':

    
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

    id_p = 'n'

    while id_p == 'n':
        try:
        
            cont_p = db.select_feed()
            id_p = input("Type it ID or (n) for new feed: ")

            if id_p == 'n' or id_p == 'N':

                url = input("Insert Feed URL: ")

                try:

                    d = feedparser.parse(url)
                    print(d.feed.title_detail)
                    link_p = d.feed.title_detail.base
                    title_p = d.feed.title_detail.value
                    url_site =  d.feed.link
                    db.insert_feed(title_p,url_site,link_p)
                    os.system('clear')

                except AttributeError:

                    os.system('clear')
                    print("Link de feed invalido")
            else:

                url = db.select_feedpod(id_p)

        except IndexError:

            os.system('clear')
            print("Id nao encontrado")
            id_p = 'n'   
    
    while 1:

        search  = input ("Episode name: ")
        search = str.title(search)




        mp3, name_mp3, error_search = m.pesquisa_pod(m.feed_in(url),search)
        
        if error_search != 1:
            break
        
        os.system('clear')
        print('Episodio Nao Encontrado!')

            
    print ("\n{}\n".format(name_mp3))
    dow = input("Want to Do Download this podcast ( Yes / No) : ")
    dow = str.upper(dow)

    if dow == "YES":

        print ("Downloading..... ")
        m.download(name_mp3,m.limpar_link(mp3))

    print("Exiting....")
    
