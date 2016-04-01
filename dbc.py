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

        
        conn = sqlite3.connect('feed_list.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
                SELECT * FROM feed ORDER BY id;
                """)
        
        print('Tabelas:')
        print("\tID\tPodCast\t\t\tLink Site\t\tURL Feed")
        print("-"*89)
        for linha in cursor:
            print('| \t{}\t{}\t{}\t{}\t|'.format(linha[0],linha[1],linha[2],linha[3]))
            '''
            print('-'*10)
            print('ID: %s' % (linha[0],))
            print('Nome: %s' % (linha[1],))
            print( 'Tel: %s' % (linha[2],))
             '''
        
            
                     
        conn.close()
