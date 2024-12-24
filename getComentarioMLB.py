import requests
from bs4 import BeautifulSoup
import json

def getMLB(nomeProduto):
    #Esse primeiro Get ele vai pegar os anuncios que tem relação com oq o usuario escreveu
    produto = requests.get("https://api.mercadolibre.com/sites/MLB/search?q="+nomeProduto)   
    
    #Validacao do primeiro GET
    if produto.status_code ==200:
        jsonProd = produto.json()

        #Esse FOR ele mostra todos os primeiros 10 anuncios relacioandos com o primeiro GET
        for i in range (10):
            print(str(i)+" = "+jsonProd["results"][i]["title"])
        #Aqui vai ser solicitado qual dos anuncios ele quer pegar os comentarios
        codProd = int(input("Escolha o produto q deseja: "))
        prodAnuncio = jsonProd["results"][codProd]["permalink"]
        print(prodAnuncio)

        #Get da pagina do anuncio solicitado pelo usuario
        anuncio = requests.get(prodAnuncio)


        #Validação do segundo GET 
        if anuncio.status_code==200 : 

            soup = BeautifulSoup(anuncio.content,'html.parser')

            #Aqui ele vai pegar todos os elementos P com a Class determina na pagina do anuncio que seria onde fica os comentarios, para ter certezar usar a inspecao de elementos do navegardor e procurar pela class abaixo
            comentarios = soup.find_all('p',{'class':'ui-review-capability-comments__comment__content ui-review-capability-comments__comment__content'})

            #Criando a lista dos comentarios
            all_p = []
            #Adicionando os comentarios a lista
            for p in comentarios:
                all_p.append(p.text)

            #Validando se o anuncio tem comentarios
            if all_p != []:
                #Mostrando os comentarios do anuncio
                for texto in all_p:
                    print("-------------------------------------------")
                    print(texto)
                    print("-------------------------------------------")
            else:
                print("Anuncio n possui comentarios")
        else:
            print('Erro '+str(anuncio.status_code))

getMLB(str(input("informe nome de um produto: ")))
