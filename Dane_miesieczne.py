import pandas as pd
import numpy as np
import openpyxl
import datetime

sciezka_fv = input('Podaj ścieżkę do pliku z falownika: ') # C:/Users/KolodTad/Desktop/Fotovolt/FalownikSF4ES008L9F256-Statystyki dzienne-20210317.xlsx
plik_fv = pd.read_excel(sciezka_fv, parse_dates=['Zaktualizowany czas'])
plik_fv['Zaktualizowany czas'] = pd.to_datetime(plik_fv['Zaktualizowany czas']).dt.date

sciezka_tauron = input('Podaj ścieżkę do pliku z Tauronu: ')
plik_tauron = pd.read_excel(sciezka_tauron, parse_dates=['Zaktualizowany czas'])
plik_tauron['Zaktualizowany czas'] = pd.to_datetime(plik_tauron['Zaktualizowany czas']).dt.date

nowy_plik_fv = plik_fv[['Zaktualizowany czas','Produkcja(kWh)']]
nowy_plik_tauron = plik_tauron[['Zaktualizowany czas','Pobór energii [kWh]','Generacja [kWh]']]

#nowy_plik_fv.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/plik_docelowy_fv.xlsx')
#nowy_plik_tauron.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/plik_docelowy_tauron.xlsx')

print(nowy_plik_fv)
print(nowy_plik_tauron)

left = pd.DataFrame(nowy_plik_fv)
right = pd.DataFrame(nowy_plik_tauron)
nowy_plik = pd.merge(left, right, on="Zaktualizowany czas")
nowy_plik.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/plik_docelowy.xlsx')

print(nowy_plik)

