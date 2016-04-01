import feedparser
import urllib
import urllib.request
import sqlite3

class DBconnect(object):

    def insert_feed(self,nome,url,link):
        print(nome)
        print(url)
        print(link)
        #lista = [(nome,url,link)]
               

        conn = sqlite3.connect('feed_list.db')
        cursor = conn.cursor()

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO feed (nome,url,link)
                VALUES (?,?,?)
                """,nome,url,link)
        conn.close()
    def select_feed(self):
        print("teste")
        # lendo os dados
        conn = sqlite3.connect('feed_list.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT id,nome FROM feed;
        """)
        for linha in cursor.fetchall:
            print(linha[0])
            print(linha[1])
            print(linha[2])
             
        conn.close()

        #conn.close()
    #select_feed()
    '''# conectando BD
    conn = sqlite3.connect('feed_list.db')
    cursor = conn.cursor()
    conn = sqlite3.connect('feed_list.db')
    cursor = conn.cursor()

    url = 'feeds.feedburner.com/hack-n-cast'
    url_feed(url)
    print(select_feed())

    conn.close()'''
