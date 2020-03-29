# Practica-1-Sraping
## Español
Scraper de datos basado en estadísticas de fútbol  escrito con python en el contexto de la asignatura "Tipología de datos y ciclo de vida de los datos" para el máster de ciencia de datos en la Universitat Oberta de Catalunya
Para ejecutar el script es necesario importar las siguientes librerías que aparecen en el fichero `requirements.txt`:
```
beautifulsoup4==4.8.1
numpy==1.17.3
pandas==0.25.3
python-dateutil==.8.1
requests==2.22.0
urllib3==1.25.6

```
Pueden instalarse fácilmente utilizando:
```shell script
pip install -r requirements.txt
```

El script se debe ejecutar de la siguiente manera:
```
python main.py


Donde **player.csv** es un csv con cabecera (con ";" como delimitador) donde la primera columna son los nombres 
que se desean scrapear.

Se generaran dos ficheros csv en la carpeta `csv`. 
```
player.csv
team.csv
