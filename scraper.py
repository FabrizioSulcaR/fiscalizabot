from bs4 import BeautifulSoup
import json
import requests
import pandas as pd
from datetime import date
from fake_headers import Headers

class Scraper:
    def __init__(self):
        pass
    
    def scraping(self):
        headers = Headers(headers=True).generate()
        link = 'https://appw.presidencia.gob.pe/visitas/transparencia/'
        HTML = BeautifulSoup((requests.get(link, headers=headers).content), 'html.parser')
        HTML = HTML.select('tr')[6]
        HTML = HTML.find_all_next('tr')
        fecha = [x.get_text() for x in sum([HTML[len(HTML)-i-1].find_all('td')[1::11] for i in range(len(HTML))],[])]
        visitante = [x.get_text() for x in sum([HTML[len(HTML)-i-1].find_all('td')[2::11] for i in range(len(HTML))],[])]
        documento = [x.get_text() for x in sum([HTML[len(HTML)-i-1].find_all('td')[3::11] for i in range(len(HTML))],[])]
        entidad = [x.get_text() for x in sum([HTML[len(HTML)-i-1].find_all('td')[4::11] for i in range(len(HTML))],[])]
        motivo = [x.get_text() for x in sum([HTML[len(HTML)-i-1].find_all('td')[5::11] for i in range(len(HTML))],[])]
        empleado_publico = [x.get_text() for x in sum([HTML[len(HTML)-i-1].find_all('td')[6::11] for i in range(len(HTML))],[])]
        oficina_cargo = [x.get_text() for x in sum([HTML[len(HTML)-i-1].find_all('td')[7::11] for i in range(len(HTML))],[])]
        hora_ingreso = [x.get_text() for x in sum([HTML[len(HTML)-i-1].find_all('td')[8::11] for i in range(len(HTML))],[])]
        hora_salida = [x.get_text() for x in sum([HTML[len(HTML)-i-1].find_all('td')[9::11] for i in range(len(HTML))],[])]
        observacion = [x.get_text() for x in sum([HTML[len(HTML)-i-1].find_all('td')[10::11] for i in range(len(HTML))],[])]

        df = {'Fecha':fecha, 'Visitante':visitante, 'Documento':documento, 'Entidad':entidad, 'Motivo':motivo, 'Empleado_publico':empleado_publico, 'Oficina_cargo': oficina_cargo, 'Hora_ingreso':hora_ingreso, 'Hora_salida':hora_salida, 'Observacion':observacion}

        df = pd.DataFrame(data=df)
        
        return df
        
    def save_info(self,df):
        results = df.to_json(orient="records")
        parsed = json.loads(results)
        with open('db.json','r',encoding='utf-8') as file:
            data = json.load(file)
            data.extend(parsed)
            res = []
            [res.append(x) for x in data if x not in res]
        with open('db.json','w', encoding='utf-8') as file:
            json.dump(res, file,ensure_ascii=False, indent=4)
        return True  

    def compute(self):
        x = Scraper()
        y = x.scraping()
        x.save_info(y)
        return True

class Filter:
    def __init__(self):
        pass
    
    def read_info(self):
        with open("db.json", "r", encoding="utf8") as f:
            data = json.load(f)
        with open("db.json", "w", encoding="utf8") as f:
            res = []
            [res.append(x) for x in data if x not in res]
            json.dump(res, f,ensure_ascii=False, indent=4)
        return data
    
    def searcher_visitas(self,data):
        today = date.today().strftime("%d/%m/%Y")
        data = list(filter(lambda x: x['Fecha']==str(today), data))
        db_visitas = [data[i] for i in range(len(data)) if data[i]['Oficina_cargo'] == 'PRESIDENCIA DE LA REPÚBLICA']
        with open('visitas_presidenciales.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            data.extend(db_visitas)
            res = []
            [res.append(x) for x in data if x not in res]
        with open('visitas_presidenciales.json', 'w', encoding='utf-8') as f:
            json.dump(res, f,ensure_ascii=False, indent=4)
        return True
    
    def compute(self):
        x = Filter()
        y = x.read_info()
        x.searcher_visitas(y)
        return True