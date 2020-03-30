import time
import requests
import json
from bs4 import BeautifulSoup

def playerScraper (diccionario_id_jugadores,headers):
    rows=[]
    iniciourl='https://www.sofascore.com/es/jugador/'
    iniciourlstds='https://www.sofascore.com/player/'
     

    
    # Para 1 equipo
    for key in diccionario_id_jugadores.keys():
        row=[]
        print('Extracting %s stats...' % key)
        row.append(key)
        url=iniciourl+key+'/'+diccionario_id_jugadores[key]
        # Wait for 0.55 seconds
        time.sleep(0.55)
        #Información del jugador
        req = requests.get(url) 
        html = BeautifulSoup(req.text, "html.parser")
        equipo =html.find('h3', {'class': 'styles__TeamLink-sc-1ss54tr-7 hUZGuP'}).getText()
        row.append(equipo)
        for infoplayer in html.find_all(class_="styles__DetailBoxTitle-sc-1ss54tr-5 enIhhc"):
            #print(infoplayer.text)
            row.append(infoplayer.text)

        #Poner none algun dato que no este, es decir de la posicion 0 a la 8 todo tiene que estar informado.
        for i in range(9-len(row)):
            row.append('None')

        #print(row)
        time.sleep(0.77)
        # Sacar estadisticas por jugador
        url=iniciourlstds+diccionario_id_jugadores[key]+'/statistics/json'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        json_object = json.loads(r.content)




        if len(json_object['statistics']) == 0:
            for stats in headers[9:]:
                row.append('?')
        else:
            for tournament in json_object['statistics'][0]['seasons'][0]['statistics']:
                for stats in tournament.keys(): 
                    if stats in headers:
                        #print (tournament[stats]) 
                        row.append(tournament[stats])

        
        rows.append(row)
    return rows