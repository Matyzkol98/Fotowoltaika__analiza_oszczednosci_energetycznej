import pandas as pd
import numpy as np
from Pobierz_plik_fv import plik_fotowoltaika_godzinowe
from Pobierz_plik_tauron import plik_tauron_godzinowe


# --------- funkcja pobieranie pliku z falownika ---------
plik_fotowoltaika_godzinowe()
#print(plik_fotowoltaika_godzinowe())

# --------- funkcja pobieranie pliku z Tauron ---------
plik_tauron_godzinowe()








'''from datetime import datetime, timedelta
import pprint

#f=pd.read_excel("C:/Users/KolodTad/Desktop/Fotovolt/Falownik.xlsx")
#for i in f["Zaktualizowany czas"]:
#  print(i)
#  print(f["Energia wytworzona dzisiaj(kWh)"])

# -------------- agregowanie danych falownika ---------------------
falownik=pd.read_excel("C:/Users/KolodTad/Desktop/Fotovolt/Falownik.xlsx")
falownik_time_list=[]
for i in falownik["Zaktualizowany czas"]:
  falownik_time_list.append(datetime.strptime(i, '%Y/%m/%d %H:%M:%S'))
print(falownik_time_list)
falownik["Zaktualizowany czas"]=falownik_time_list
falownik.resample('H',on="Zaktualizowany czas").sum().to_excel("C:/Users/KolodTad/Desktop/Fotovolt/falownik_aggr.xlsx")

#--------------- import i formatowanie danych falownika i energetyka -------------------
falownik=pd.read_excel("C:/Users/KolodTad/Desktop/Fotovolt/falownik_aggr.xlsx")
falownik_time_list=[]
for i in falownik["Zaktualizowany czas"]:
  falownik_time_list.append(datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S'))
#print(falownik_time_list)
falownik["Zaktualizowany czas"]=falownik_time_list
dict_falownik=dict(zip(falownik["Zaktualizowany czas"], falownik["Energia wytworzona dzisiaj(kWh)"]))
for i in dict_falownik.keys():
  print(i, dict_falownik[i])

energetyk=pd.read_excel("C:/Users/KolodTad/Desktop/Fotovolt/dane_dobowe.xlsx")
energetyk_time_list=[]
for i in energetyk["Data, godzina"]:
  energetyk_time_list.append(datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S'))
dict_energetyk=dict(zip(energetyk_time_list, energetyk["Pobór energii [kWh]"]))
for i in dict_energetyk.keys():
  print(i, dict_energetyk[i])
  if i in dict_falownik:
    print(dict_falownik[i])
#
'''