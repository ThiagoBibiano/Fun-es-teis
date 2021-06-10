"""
Created on Wed Jun  9 21:00:09 2021

@author: Thiago Bibiano
"""


import requests
from bs4 import BeautifulSoup

def url_de_busca(protocolo: str):
    protocolo2 = protocolo.replace("%","/")
    return f"http://www.imprensaoficial.com.br/DO/BuscaDO2001Resultado_11_3.aspx?filtropalavraschave={protocolo2}&f=xhitlist&xhitlist_vpc=first&xhitlist_x=Advanced&xhitlist_q=({protocolo})&xhitlist_mh=9999&filtrotipopalavraschavesalvar=UP&filtrotodoscadernos=True&xhitlist_hc=%5bXML%5d%5bKwic%2c3%5d&xhitlist_vps=15&xhitlist_xsl=xhitlist.xsl&xhitlist_s=&xhitlist_sel=title%3bField%3adc%3atamanho%3bField%3adc%3adatapubl%3bField%3adc%3acaderno%3bitem-bookmark%3bhit-context"

def extrai_data_pagina_e_caderno(tipo: str, link: str):
    for txt in str(link).split("&"):
        if tipo in txt:
            return txt.split("=")[-1]


prt = "6058.2020/0002592-7"
page = requests.get(url_de_busca(prt))
coleta = BeautifulSoup(page.text, 'html.parser')

for link in coleta.findAll('a', href=True):
    if "bg-light text-dark" in str(link):
        print(prt)
        print(link.text)
        print("http://www.imprensaoficial.com.br" + link["href"])
        print(extrai_data_pagina_e_caderno("data", link))
        print(extrai_data_pagina_e_caderno("caderno", link))
        print(extrai_data_pagina_e_caderno("pagina", link))
