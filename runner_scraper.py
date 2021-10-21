from scraper import Scraper, Filter
import time

inicio = time.time()
x = Scraper()
y = Filter()

x.compute()
y.compute()

final = time.time()
print('Bases de datos actualizadas')
print("TIEMPO DE EJECUCIÓN",final-inicio)