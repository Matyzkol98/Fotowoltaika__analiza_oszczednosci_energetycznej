# --------- import modułów ---------
from IPython.display import display
import pandas as pd
import numpy as np
import openpyxl
import datetime


# --------- pobieranie pliku z falownika ---------
# sciezka_fv = input('Podaj ścieżkę do pliku z falownika: ')
plik_fv = pd.read_excel('C:/Users/KolodTad/Desktop/Fotovolt/FalownikSF4ES008L9F256-Statystyki dzienne-20210317.xlsx',
                        parse_dates=['Zaktualizowany czas'])
plik_fv['Zaktualizowany czas'] = pd.to_datetime(plik_fv['Zaktualizowany czas']).dt.date
plik_fv['Dzień tygodnia'] = pd.to_datetime(plik_fv['Zaktualizowany czas']).dt.day_name()


# --------- pobieranie pliku z Tauron ---------
# sciezka_tauron = input('Podaj ścieżkę do pliku z Tauronu: ')
plik_tauron = pd.read_excel('C:/Users/KolodTad/Desktop/Fotovolt/dane.xlsx', parse_dates=['Zaktualizowany czas'])
plik_tauron['Zaktualizowany czas'] = pd.to_datetime(plik_tauron['Zaktualizowany czas']).dt.date

# --------- przekształcenia plików ---------
nowy_plik_fv = plik_fv[['Zaktualizowany czas', 'Dzień tygodnia', 'Produkcja(kWh)']]
nowy_plik_tauron = plik_tauron[['Zaktualizowany czas', 'Pobór energii [kWh]', 'Generacja [kWh]']]

# nowy_plik_fv.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/plik_docelowy_fv.xlsx')
# nowy_plik_tauron.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/plik_docelowy_tauron.xlsx')

#print(nowy_plik_fv)
#print(nowy_plik_tauron)

# --------- sklejenie plików w nowy plik ---------
left = pd.DataFrame(nowy_plik_fv)
right = pd.DataFrame(nowy_plik_tauron)
nowy_plik = pd.merge(left, right, on="Zaktualizowany czas")
# nowy_plik.to_excel('/content/drive/MyDrive/Fotovoltaika/plik_docelowy.xlsx')

# --------- utworzenie nowych kolumn ---------
nowy_plik['Zużytkowano z FV [kWh]'] = np.float_()   # NaN - trzeba było zamienic na typ float dla tych kolumn
nowy_plik['Zużycie dom [kWh]'] = np.float_()        # inaczej kolumny poniżej się nie liczyły matematycznie

# --------- zaindeksowanie kolumn do operacji matematycznych ---------
index_produkcja = nowy_plik.columns.get_loc('Produkcja(kWh)')
index_generacja = nowy_plik.columns.get_loc('Generacja [kWh]')
index_pobor = nowy_plik.columns.get_loc('Pobór energii [kWh]')
index_total = nowy_plik.columns.get_loc('Zużytkowano z FV [kWh]')
index_zuzycie = nowy_plik.columns.get_loc('Zużycie dom [kWh]')

# print(index_produkcja,index_generacja,index_total,index_max)

# --------- operacje matematyczne wyliczania dla nowych kolumn ---------
for row in range(0, len(nowy_plik)):
    nowy_plik.iat[row, index_total] = nowy_plik.iat[row, index_produkcja] - nowy_plik.iat[row, index_generacja]
    nowy_plik.iat[row, index_zuzycie] = nowy_plik.iat[row, index_total] + nowy_plik.iat[row, index_pobor]
#nowy_plik.loc['Suma:'] = pd.Series(nowy_plik['Zużytkowano z FV [kWh]'].sum(), index = ['Zużytkowano z FV [kWh]'])
nowy_plik.loc['Suma:'] = nowy_plik.select_dtypes(pd.np.number).sum()

def highlight_max(s):
    is_max = s == s.max()
    return ['background-color: yellow' if v else '' for v in is_max]

nowy_plik.style.apply(highlight_max)

display(nowy_plik)

# --------- zapis do nowego pliku zagregowanych danych ---------
nowy_plik.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/plik_docelowy.xlsx')