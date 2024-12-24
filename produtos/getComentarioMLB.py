import requests
from bs4 import BeautifulSoup

def mlbanuncio(link,h1,clas):
    anuncio = requests.get(link)
    if anuncio.status_code==200:
        soup = BeautifulSoup(anuncio.content,'html.parser')
        text = soup.find_all(h1,{'class':clas})

        all_titulo =[]

        for t in text:
            all_titulo.append(t.text)    
        return all_titulo
    else:
        return 'sem acesso ao anuncio'
    
def mlbanuncio2(link,h1,clas,subclass):
    anuncio = requests.get(link)
    if anuncio.status_code==200:
        soup = BeautifulSoup(anuncio.content,'html.parser')
        text = soup.find_all(h1,{'role':subclass,'class':clas})

        all_titulo =[]

        for t in text:
            all_titulo.append(t.text)    
        return all_titulo
    else:
        return 'sem acesso ao anuncio'
    

def getMLB(nomeProduto):
    #Esse primeiro Get ele vai pegar os anuncios que tem relação com oq o usuario escreveu
    produto = requests.get("https://api.mercadolibre.com/sites/MLB/search?q="+nomeProduto)   
    
    #Validacao do primeiro GET
    if produto.status_code ==200:
        jsonProd = produto.json()
        lista = []
        
        #Esse FOR ele mostra todos os primeiros 10 anuncios relacioandos com o primeiro GET
        if len(jsonProd["results"]) == 0:
            return 'sem acesso ao anuncio'
        for i in range (12):
            lista.append(jsonProd["results"][i])
        return lista
    else:
        return 'sem acesso ao anuncio'
