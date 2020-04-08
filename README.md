# Practica-1-Scraping

## Español
Scraper de datos basado en estadísticas de fútbol  escrito con python en el contexto de la asignatura "Tipología de datos y ciclo de vida de los datos" para el máster de ciencia de datos en la Universitat Oberta de Catalunya
Para ejecutar el script es necesario importar las siguientes librerías que aparecen en el fichero `requirements.txt`:
```
beautifulsoup4==4.7.1
pandas==0.24.2
requests==2.21.0
urllib3==1.24.1

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

Se generara un fichero csv en la carpeta `csv`. Stats_Players_LaLiga_19_20.csv


2 ficheros .py que contiene la carpeta src. main.py. playerScraper.
```



