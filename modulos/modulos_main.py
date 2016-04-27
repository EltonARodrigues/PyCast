import feedparser
import urllib
import urllib.request


class Modulos:

    def feed_in(self,url):

        if str.find(url,"http://") !=  False:
            url = "http://" + url
        print("Carregando feed...")
        d = feedparser.parse(url)
        n_epsodes = int((len(d['entries'])))

        return d, n_epsodes

    def download(self,name,file):

        html=urllib.request.urlopen(file).read()

        if str.find(name,".mp3") == False:
            name = name + ".mp3"

        arq = open(name, "wb")
        arq.write(html)
        arq.close()

    def limpar_link(self,mp3):

        mp3 =mp3.split(".mp3")[0]
        mp3 = mp3.split("http://")[-1]

        if str.find(mp3,"http://") !=  0:
            mp3 = "http://" + mp3


        if str.find(mp3,".mp3") == -1:
            mp3 = mp3 + ".mp3"

        return mp3

    def pesquisa_pod(self,feed,search):

        d, n_epsodes = feed
        list_q = {}
        quant_episodes = 0
        error_search = 0

        for i in range(n_epsodes):
            titulo = (d['entries'][i]['title'])
    
            if str.find(str.upper(titulo),str.upper(search)) != -1:
               
                search_value = i
                list_q[int(quant_episodes)] = i
                quant_episodes +=  1
                
                print ("|{}|".format(i)," {}".format(d['entries'][i]['title']))

        if quant_episodes > 1:

            choice = input("Escolha um episódio pelo ID: ")

            for quant in range(0,quant_episodes):

                if list_q[quant]==choice:
                    search_value = int(choice)

        elif quant_episodes < 1: 

            error_search = 1
            mp3 = None
            name = None
            
        if error_search != 1:

            mp3 = str(d['entries'][search_value]['enclosures'])
            name = str(d['entries'][search_value]['title'])

        return mp3, name, error_search
        
        
        
        
