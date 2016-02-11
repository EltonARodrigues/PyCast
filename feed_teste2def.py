import feedparser
import urllib
import string
import urllib.request
import string
from array import array

def feed_in(url):


    if str.find(url,"http://") !=  0:
        url = "http://" + url
    print("Carregando feed....")
    d = feedparser.parse(url)
    d.feed.title
    d.feed.link
    d.feed.subtitle
    d.feed.url
    nprogramas = int((len(d['entries'])))

    return d, nprogramas

def download(nome,arquivo):
    html=urllib.request.urlopen(arquivo).read()

    if str.find(nome,".mp3") == -1:
        nome = nome + ".mp3"

    arq = open(nome, "wb")
    arq.write(html)
    arq.close()



def limpar_link(mp3):
    mp3 =mp3.split(".mp3")[0]
    mp3 = mp3.split("http://")[-1]

    if str.find(mp3,"http://") !=  0:
        mp3 = "http://" + mp3


    if str.find(mp3,".mp3") == -1:
        mp3 = mp3 + ".mp3"

    return mp3



contador = 0
t=0
lista = {}
url = "http://feeds.feedburner.com/rapaduracast"
#url = input("Insira link do site: ")
d, nprogramas = feed_in(url)



pesquisa  = input("Nome do EP: ")
pesquisa = str.title(pesquisa)

for i in range(nprogramas):

    #print(d['entries'][i]['title'])
    titulo = (d['entries'][i]['title'])
    #mp3 = str(d['entries'][40]['media_content'])

    if str.find(titulo,pesquisa) != -1:
        contador = contador + 1
        valor_pesquisa = i

        lista[int(t)] = i
        t = t + 1
        #print(d['entries'][i]['title'])


#if contador > 1:
#    escolha = input("Mais de uma resultado enconrado.. insira o numero de um dos eps encotrados: ")
#    print(lista[1])
    #if str.find(titulo,escolha) != -1:
        #print(d['entries'][]['title'])


#print(int(escolha))
#nome = d['entries'][int(escolha)]['title']
#print(nome)

mp3 = str(d['entries'][valor_pesquisa]['media_content'])
nome = d['entries'][valor_pesquisa]['title']
print(nome)
print(limpar_link(mp3))

dow = input("Deseja realizar o download desse podcast(sim/nao): ")
dow = str.upper(dow)

if dow == "SIM":

    print ("Realizando Download.......")
    download(nome,limpar_link(mp3))

print("saindo....")

#except NameError:
#    print("Nome não encontrado...realizar pesquisa novamentes")
