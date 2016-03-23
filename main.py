# -*- coding: utf-8 -*-
import feedparser
import urllib
import urllib.request
from modulos.modulos_main import Modulos
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

    url = input("Insira URL do feed: ")
    #url = 'http://feeds.feedburner.com/jack-animeclub'
    #url = "http://feed.nerdcast.com.br"

    pesquisa  = input ("Nome do EP: ")
    pesquisa = str.title(pesquisa)

    nome_mp3, mp3 = m.pesquisa_pod(m.feed_in(url),pesquisa)
    #print ("\n{}\n".forma(nome_mp3))

    dow = input("Deseja realizar o download desse podcast(sim/nao): ")
    dow = str.upper(dow)

    if dow == "SIM":

        print ("Realizando Download...")
        m.download(nome_mp3,m.limpar_link(mp3))

    print("Saindo....")
