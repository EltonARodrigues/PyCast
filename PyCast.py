# -*- coding: utf-8 -*-

from XMLCSV.XMLdata import XMLdata
from XMLCSV.OPML import OPML
from XMLCSV.csv_import import CSVfeed
import os

class Pycast(object):
   
    def __init__(self):
        self.url = str
        self.exit = False
        self.id_p = 'continue'

    def main(self):
        while self.id_p == 'continue':
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
                    
                    self.id_p = input("\nType it ID or new/import/remove/exit feed: ")
                    if type(self.id_p) is str:
                        self.id_p = self.id_p.lower()

                if self.id_p == 'new' or self.id_p == 'continue':

                    self.url = input("Insert Feed URL: ")
                    
                    if str.find(self.url, "https://") != 0:
                        if str.find(self.url, "http://") != 0:
                            self.url = "http://" + self.url

                    if CSV.verify(self.url) is True:
                        os.system('clear')
                        print('\t\t\t\t\tFeed already added')
                    
                    else:
                        XMLdata(self.url).add_feed()
                    self.id_p = 'continue'
                    os.system('clear')

                elif(self.id_p == 'import'):
                    
                    try:
                        file = input("Arraste o arquivo ou digite o caminho do OPML:")
                        OPML(file).get_opml()
                        os.system('clear')
                        print('\t\t\t\t\tImport successfully')
                        self.id_p = 'continue'
                    
                    except FileNotFoundError:
                        os.system('clear')
                        print('\t\t\t\t\tFile not Found!!!')
                        self.id_p = 'continue'
                    
                elif self.id_p == 'remove':
                    id_remove = input("Insert ID to remove feed: ")
                   
                    CSV.remove(id_remove)
                    os.system('clear')
                    self.id_p = 'continue'
               

                elif self.id_p == 'exit':
                    return True

                elif self.id_p.isdigit() == True:
                    self.url = CSV.get_url(self.id_p)

                else:
                    self.id_p = 'continue'
                    os.system('clear')
                    self.id_p = 'continue'
                    print('\t\t\t\t\tinput invalid!')

            except IndexError:

                os.system('clear')
                print("\t\t\t\t\tID not found")
                self.id_p = 'continue'

            except AttributeError:
                os.system('clear')
                print("\t\t\t\t\tfeed link invalid")
                self.id_p = 'continue'

        

        print('Loading...')
        try:
            while 1:
                m = XMLdata(self.url)
                search = input('Type episode name or restart: ')
                search = str.title(search)

                if search == 'Restart':
                    break

                mp3, name_mp3, error_search = m.search_pod(m.feed_in(), search)
                
                if error_search != 1:
                    break

                os.system('clear')
                print('\t\t\t\t\tEpisode not found!')

            if search != 'Restart':
                dow = input("Want to Do Download this podcast ( Yes / No) : ")
                dow = str.upper(dow)

                if dow == "YES":

                    print("Downloading..... ")

                    podcast_name = m.title_p
                    m.download(name_mp3, m.clear_link(mp3), podcast_name)
                    self.id_p = 'continue'
                    os.system('clear')
                    print('\tDownload Complete - ' + name_mp3)

                elif dow == 'NO':
                    self.id_p = 'continue'
                    os.system('clear')
            else:
                self.id_p = 'continue'
                os.system('clear')   

        except AttributeError:
            os.system('clear')
            print("\t\t\t\t\tID not found")
            self.id_p = 'continue'

        return False

if __name__ == '__main__':
    P = Pycast()
    os.system('clear')
    while 1:
        if P.main() == True:
            break
