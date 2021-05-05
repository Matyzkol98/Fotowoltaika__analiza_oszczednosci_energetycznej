import pandas as pd
import numpy as np
import ChangeExcel
import Pobierz_plik
import XLSX_to_DB

# --------- przekształcenia plików wsadowych z pobraniem plików z Falownika i Tauron ---------
nowy_plik_fv = Pobierz_plik.Plikfotowoltaika.plik_fotowoltaika_godzinowe()[['Data', 'Energia wytworzona dzisiaj(kWh)']]
new_bid = []
x = 0
for index, row in nowy_plik_fv.iterrows():
    y = row['Energia wytworzona dzisiaj(kWh)']
    if y > 0:
        new_bid.append(y-x)
        x = row['Energia wytworzona dzisiaj(kWh)']
    else:
        new_bid.append(0)
        x = 0
nowy_plik_fv['Przyrost'] = new_bid
nowy_plik_fv = nowy_plik_fv.resample('H', on='Data').Przyrost.sum()

nowy_plik_tauron = Pobierz_plik.Pliktauron.plik_tauron_godzinowe()[['Data', 'Dzień tygodnia', 'Pobór energii [kWh]', 'Oddanie [kWh]']]

# --------- sklejenie plików w nowy plik ---------
right = pd.DataFrame(nowy_plik_fv)
left = pd.DataFrame(nowy_plik_tauron)
nowy_plik = pd.merge(left, right, on='Data', how="outer")
nowy_plik.rename(columns={'Przyrost':'Produkcja [kWh]'}, inplace=True)
nowy_plik = nowy_plik.replace(np.NaN, 0)

# --------- utworzenie nowych kolumn ---------
nowy_plik['Zużytkowano z FV [kWh]'] = np.float_()   # NaN - trzeba było zamienic na typ float dla tych kolumn
nowy_plik['Zużycie dom [kWh]'] = np.float_()        # inaczej kolumny poniżej się nie liczyły matematycznie

# --------- zaindeksowanie kolumn do operacji matematycznych ---------
index_produkcja = nowy_plik.columns.get_loc('Produkcja [kWh]')
index_oddanie = nowy_plik.columns.get_loc('Oddanie [kWh]')
index_pobor = nowy_plik.columns.get_loc('Pobór energii [kWh]')
index_total = nowy_plik.columns.get_loc('Zużytkowano z FV [kWh]')
index_zuzycie = nowy_plik.columns.get_loc('Zużycie dom [kWh]')

# --------- operacje matematyczne - wyliczania dla nowych kolumn ---------
for row in range(0, len(nowy_plik)):
    nowy_plik.iat[row, index_total] = nowy_plik.iat[row, index_produkcja] - nowy_plik.iat[row, index_oddanie]
    nowy_plik.iat[row, index_zuzycie] = nowy_plik.iat[row, index_total] + nowy_plik.iat[row, index_pobor]

# ------------ tworzenia pliku DB -------------
sql_plik = nowy_plik
sql_plik.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/temp/plik_dla_DB_godzinowy.xlsx')
XLSX_to_DB.Xlsxtodb.db_godzinowe()
# -----------------------------------------------------------------------------------------------------------------

ChangeExcel.colormaxmin_sum_godzinowy(nowy_plik)

