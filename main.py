# -*- coding: utf-8 -*-
#python_version  :3.4
import feedparser
import urllib
import urllib.request

def feed_in(url):

    if str.find(url,"http://") !=  False:
        url = "http://" + url
    print("Carregando feed...")
    d = feedparser.parse(url)
    d.feed.title
    d.feed.link
    d.feed.subtitle
    d.feed.url
    nprogramas = int((len(d['entries'])))

    return d, nprogramas

def download(nome,arquivo):
    html=urllib.request.urlopen(arquivo).read()

    if str.find(nome,".mp3") == False:
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

###############################################################################


t=0
lista = {}
lista_de_escolha = []
numeros = 0

url = 'feeds.feedburner.com/hack-n-cast'
#url = input("Insira link do site: ")

d, nprogramas = feed_in(url)

pesquisa  = input ("Nome do EP: ")
pesquisa = str.title(pesquisa)


print ('- ID - ')
try:
    for i in range(nprogramas):

        titulo = (d['entries'][i]['title'])

        if str.find(titulo,pesquisa) != -1:

            valor_pesquisa = i
            lista[int(t)] = i
            t += 1
            lista_de_escolha += [i]
            numeros +=  1
            print ('"',i,'" | ',d['entries'][i]['title'])


    if numeros > 1:

        escolha = 0
        escolha = input("Escolha um episódio pelo ID: ")
        escolha = int(escolha)
        valor_pesquisa = 'vazio'

        for c in range(0,numeros):

            if lista_de_escolha[c]==escolha:
                valor_pesquisa = escolha

        if valor_pesquisa == 'vazio':
            print ('Escolha não existe')
            exit()


    mp3 = str(d['entries'][valor_pesquisa]['media_content'])
    nome = d['entries'][valor_pesquisa]['title']


    print (nome)

    dow = input("Deseja realizar o download desse podcast(sim/nao): ")
    dow = str.upper(dow)

    if dow == "SIM":

        print ("Realizando Download...")
        download(nome,limpar_link(mp3))

    print("Saindo....")

except NameError:
    print("Nome não encontrado...realizar pesquisa novamentes")
