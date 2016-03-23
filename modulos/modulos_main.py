import feedparser
import urllib
import urllib.request


class Modulos:

    def feed_in(self,url):

        if str.find(url,"http://") !=  False:
            url = "http://" + url
        print("Carregando feed...")
        d = feedparser.parse(url)
        nprogramas = int((len(d['entries'])))

        return d, nprogramas

    def download(self,nome,arquivo):
        html=urllib.request.urlopen(arquivo).read()

        if str.find(nome,".mp3") == False:
            nome = nome + ".mp3"

        arq = open(nome, "wb")
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

    def pesquisa_pod(self,feed,pesquisa):
        d, nprogramas = feed
        lista = {}
        quant_resultados = 0

        #try:
        for i in range(nprogramas):

            titulo = (d['entries'][i]['title'])

            if str.find(str.upper(titulo),str.upper(pesquisa)) != -1:
                print("teste")
                valor_pesquisa = i
                lista[int(quant_resultados)] = i
                quant_resultados +=  1
                print ('"',i,'" | ',d['entries'][i]['title'])

        if quant_resultados > 1:

            escolha = input("Escolha um episódio pelo ID: ")
            #ERRO DE TIPO ARRUMAR COM escolha = int(escolha)

            for quant in range(0,quant_resultados):

                if lista[quant]==escolha:
                    valor_pesquisa = int(escolha)
                #print(lista[quant])

            if valor_pesquisa == 'vazio':
                print ('Escolha não existe')
                exit()

        mp3 = str(d['entries'][valor_pesquisa]['enclosures'])
        nome = str(d['entries'][valor_pesquisa]['title'])
        return nome, mp3
