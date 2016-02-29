import feedparser
import urllib
import urllib.request
import sqlite3

class DBconnect(object):

    def insert_feed(title,url,subtitle,link,arquivoXML):

        #if str.find(url,"http://") !=  False:
        #    url = "http://" + url

        #print("Carregando feed...")

        #d = feedparser.parse(url)
        #teste = "fdsfsdfds"
        dados = [(title,url,subtitle,link,arquivoXML)]

        # conectando BD
        #conn = sqlite3.connect('feed_list.db')
        #cursor = conn.cursor()
        # inserindo dados na tabela
        conn = sqlite3.connect('feed_list.db')
        cursor = conn.cursor()

        cursor.executemany("""
        INSERT INTO feed (nome, url, subtitle, link, arquivo_feed)
        VALUES (?,?,?,?,?)
        """,dados)

        # gravando no bd
        conn.commit()
        conn.close()

        print('Dados inseridos com sucesso.')

        #conn.close()

    def select_feed():

        # lendo os dados
        conn = sqlite3.connect('feed_list.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM feed;
        """)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()

        #conn.close()
    select_feed()
    '''# conectando BD
    conn = sqlite3.connect('feed_list.db')
    cursor = conn.cursor()
    conn = sqlite3.connect('feed_list.db')
    cursor = conn.cursor()

    url = 'feeds.feedburner.com/hack-n-cast'
    url_feed(url)
    print(select_feed())

    conn.close()'''
