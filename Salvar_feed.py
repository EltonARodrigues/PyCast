import feedparser
import urllib
import urllib.request
import sqlite3


def url_feed(url):

    if str.find(url,"http://") !=  False:
        url = "http://" + url

    print("Carregando feed...")

    d = feedparser.parse(url)

    dados = [(d.feed.title,url,d.feed.subtitle,d.feed.link)]

    # conectando BD
    #conn = sqlite3.connect('feed_list.db')
    #cursor = conn.cursor()
    # inserindo dados na tabela
    cursor.executemany("""
    INSERT INTO feed (nome, url, subtitle, link)
    VALUES (?,?,?,?)
    """, dados)

    # gravando no bd
    conn.commit()

    print('Dados inseridos com sucesso.')

    #conn.close()

def select_feed():

    # lendo os dados
    cursor.execute("""
    SELECT * FROM feed;
    """)

    for linha in cursor.fetchall():
        print(linha)

    #conn.close()

# conectando BD
conn = sqlite3.connect('feed_list.db')
cursor = conn.cursor()
conn = sqlite3.connect('feed_list.db')
cursor = conn.cursor()

url = 'feeds.feedburner.com/hack-n-cast'
url_feed(url)
print(select_feed())

conn.close()
