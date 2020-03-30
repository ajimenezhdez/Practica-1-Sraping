import urllib.request
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import json
import Scraper_player

rows = []
rowPlayer = []
consolidated = []
headers = ['Name','Team','Nac.','Age','Height','Preffoot','Position','Number','ValuePlayer','matchesTotal', 'matchesStarting',
               'minutesPerGame', 'goals', 'goalsFrequency', 'goalsAverage', 'totalShotsPerGame','bigChanceMissed']

team_links = {1:['Athletic Bilbao', 'https://www.sofascore.com/team/football/athletic-bilbao/2825'],
              2:['Atlético Madrid', 'https://www.sofascore.com/team/football/atletico-madrid/2836'],
              3:['Deportivo Alavés', 'https://www.sofascore.com/team/football/deportivo-alaves/2885'],
              4:['Leganés', 'https://www.sofascore.com/team/football/leganes/2845'],
              5:['Getafe', 'https://www.sofascore.com/team/football/getafe/2859'],
              6:['Osasuna', 'https://www.sofascore.com/team/football/osasuna/2820'],
              7:['Valencia', 'https://www.sofascore.com/team/football/valencia/2828'],
              8:['Villarreal', 'https://www.sofascore.com/team/football/villarreal/2819'],
              9:['Granada', 'https://www.sofascore.com/team/football/granada/33779'],
              10:['Barcelona', 'https://www.sofascore.com/team/football/barcelona/2817'],
              11:['Sevilla', 'https://www.sofascore.com/team/football/sevilla/2833'],
              12:['Real Valladolid', 'https://www.sofascore.com/team/football/real-valladolid/2831'],
              13:['Celta Vigo', 'https://www.sofascore.com/team/football/celta-vigo/2821'],
              14:['Espanyol', 'https://www.sofascore.com/team/football/espanyol/2814'],
              15:['Real Betis', 'https://www.sofascore.com/team/football/real-betis/2816'],
              16:['Real Madrid', 'https://www.sofascore.com/team/football/real-madrid/2829'],
              17:['Real Sociedad', 'https://www.sofascore.com/team/football/real-sociedad/2824'],
              18:['Eibar', 'https://www.sofascore.com/team/football/eibar/2839'],
              19:['Levante', 'https://www.sofascore.com/team/football/levante/2849'],
              20:['Mallorca', 'https://www.sofascore.com/team/football/rcd-mallorca/2826']}


for valor_dic_equipo in range(len(team_links)):
    print('Extrayendo IDs de los jugadores del ' + team_links[valor_dic_equipo+1][0] + '...')
    time.sleep(0.5)
    req = requests.get(team_links[valor_dic_equipo+1][1])
    html = BeautifulSoup(req.text, "html.parser")

    lista_enlaces_jugadores = []
    ini_enlace_jugadores = '/player'

    for tag_jugador in html.find_all(class_="squad__player squad-player u-tC js-show-player-modal ff-medium"):
        lista_enlaces_jugadores.append(tag_jugador.get('href'))

    lista_id_jugadores = []
    for i in lista_enlaces_jugadores:
        lista_id_jugadores.append(i[(len(ini_enlace_jugadores)+1):].split('/'))

    diccionario_id_jugadores = {}
    for i in lista_id_jugadores:
        diccionario_id_jugadores[i[0]] = i[1]
        
    #LLamar funcion de jugadores
    rowPlayer=Scraper_player.playerScraper(diccionario_id_jugadores,headers)
    rows.append(rowPlayer)

df = pd.DataFrame(columns=headers)  
for i in range (len(rows)):
    df =df.append(pd.DataFrame(rows[i], columns=headers))

consolidated.append(df)   
pd.concat(consolidated).to_csv(r'Stats_Players_LaLiga_19_20.csv', sep=',', encoding='utf-8-sig',index=False)
