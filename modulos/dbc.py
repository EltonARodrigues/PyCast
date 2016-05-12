import feedparser
import urllib
import urllib.request
import sqlite3

class DBconnect(object):

    
    def insert_feed(self,p_nome,p_url,p_link):
        print(p_nome)
        print(p_url)
        print(p_link)
        lista = [(p_nome,p_url,p_link)]
               

        conn = sqlite3.connect('feed_list.db')
        cursor = conn.cursor()
        
        # inserindo dados na tabela
 
        cursor.execute("""
                INSERT INTO feed (nome,url,link)
                VALUES (?,?,?)
                """,(p_nome,p_url,p_link))
        conn.commit()
        conn.close()

    def select_feed(self):
        cont = 0 
        
        conn = sqlite3.connect('feed_list.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("SELECT * FROM feed ORDER BY id;")
        
        print('Tabelas:')
        print("\tID\tPodCast\t")
        print("-"*39)
        for linha in cursor:
            print('|\t{}\t{}\t'.format(linha[0],linha[1]))
            cont = cont + 1
           
        conn.close()
        return cont - 1

    def select_feedpod(self,id):
        cont = 0 
        
        conn = sqlite3.connect('feed_list.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute('SELECT link FROM feed WHERE id = ?', (id,))
        link_pesq = cursor.fetchall()[0][0]

        #print(cursor.fetchall())
        #for url in cursor.fetchall():

        conn.close()
        return link_pesq

    def check_link_feed(self,url):
        cont = 0 
        
        conn = sqlite3.connect('feed_list.db')
        cursor = conn.cursor()

        # lendo os dado
        cursor.execute('''SELECT nome FROM feed WHERE link = ? ''', (url,))
        check_url = cursor.fetchone()

        conn.close()

        if check_url == None:
            return 1

        else:
            return 0    