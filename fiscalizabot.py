import json
import tweepy

API_KEY = '9ibaF7QN1evE7D9iiKEuzjkd0'
API_SECRET_KEY = 'fErUQSutaiFFT5beLZdO5cPMtRK54z1ui8nZupA1ZGi3HGYrcr'
ACCESS_TOKEN = '1449425397259673602-si8G3IJMzE3Lo3sCQblK57O0OzigGc'
ACCESS_SECRET_TOKEN = 'pfzM0kqnV1oEM4OEhkCQ9y4A1Gb9TbmkmdLzL6B0aQCpv'

auth= tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth)

class TweetBot:
    def __init__(self):
        pass
    
    def read_info(self):
        with open("visitas.json", "r", encoding="utf8") as f:
            data = json.load(f)
            print('¡Visitas cargadas!')
        return data
    
    def read_i(self):
        file1 =  open('i.txt', 'r')
        line = file1.readlines()
        return line
    
    def post(self,data,i):
        api.update_status('Reunión presidencial N° ' +str([i]+1) + ' - ' + str(data[i]['Fecha']) + '\n' +  'El presidente Pedro Castillo Terrones se reunió hoy con ' + str(data[i]['Visitante'].title()) + ', ' + str(data[i]['Entidad']) + '.' + '\n' + 'La reunión se llevó a cabo desde las ' + str(data[i]['Hora_ingreso'] + ' hasta las ' + str(data[i]['Hora_salida'])))

        print('La visita de ' + str(data[i]['Visitante']) + ' ha sido tuiteada.')
        print('\n')

    def upgrade_i(self,line):
        file1 = open('i.txt', 'w')
        file1.write(str(int(line[0])+1))
