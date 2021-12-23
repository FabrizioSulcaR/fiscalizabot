from dotenv import load_dotenv
from datetime import date
import json
import tweepy
import random
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET_TOKEN = os.getenv('ACCESS_SECRET_TOKEN')

auth= tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth)

class TweetBot:
    def __init__(self):
        pass
    
    def read_info(self):
        today = date.today().strftime("%d/%m/%Y")
        with open("visitas_presidenciales.json", "r", encoding="utf8") as f:
            data = json.load(f)
            data = list(filter(lambda x: x['Fecha']==str(today), data))
        return data
    
    def read_i(self):
        with open('i.txt', 'r', encoding='utf-8') as f:
            return f.readlines()
    
    def post(self,data,i, intros):
        api.update_status('Reunión presidencial N°' + str(int(i) +1)  + ' - ' +
                          str(data[i]['Fecha']) + '\n' +  
                          str(random.choice(intros))+
                          str(data[i]['Visitante'].title()) + ', ' +
                          str(data[i]['Entidad']) + '.' + '\n' +
                          'La reunión se llevó a cabo desde las ' +
                          str(data[i]['Hora_ingreso'] + ' hasta las ' + str(data[i]['Hora_salida'])))

        print('\n' + 'Consola:', 'La visita de ' + str(data[i]['Visitante']) + ' ha sido tuiteada.')

    def upgrade_i(self,line):
        with open("i.txt","w", encoding='utf-8') as f:
            f.write(str(int(line[0])+1))
    
    def read_intros(self):
        with open("intros.json", "r", encoding="utf-8") as f:
            intros = json.load(f)
        return intros