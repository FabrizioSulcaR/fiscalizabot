#El crontab debe ejecutarlo cada día a medianoche
with open('i.txt',"w", encoding='utf-8') as f:
    f.write('0')