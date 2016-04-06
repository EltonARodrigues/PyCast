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
        id_p = input("Digite o ID ou (n) para novo podcast: ")
        print(cont_p)
        if id_p == 'n' or id_p == 'N':

            url = 'http://feeds.feedburner.com/jack-animeclub'

            d = feedparser.parse(url)
            link_p = d.feed.title_detail.base
            title_p = d.feed.title_detail.value
            url_site =  d.feed.link
            db.insert_feed(title_p,url_site,link_p)
            os.system('clear')

        else:
            url = db.select_feedpod(id_p)


    pesquisa  = input ("Nome do EP: ")
    pesquisa = str.title(pesquisa)

    nome_mp3, mp3 = m.pesquisa_pod(m.feed_in(url),pesquisa)
    print ("\n{}\n".format(nome_mp3))

    dow = input("Deseja realizar o download desse podcast(sim/nao): ")
    dow = str.upper(dow)

    if dow == "SIM":

        print ("Realizando Download...")
        m.download(nome_mp3,m.limpar_link(mp3))

    print("Saindo....")
