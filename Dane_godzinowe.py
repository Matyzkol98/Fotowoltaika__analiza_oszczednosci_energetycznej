from xlsxwriter.utility import xl_rowcol_to_cell
import pandas as pd
import numpy as np
from Pobierz_plik_fv import plik_fotowoltaika_godzinowe
from Pobierz_plik_tauron import plik_tauron_godzinowe
from XLSX_to_DB import db_godzinowe

# --------- przekształcenia plików wsadowych z pobraniem plików z Falownika i Tauron ---------
nowy_plik_fv = plik_fotowoltaika_godzinowe()[['Zaktualizowany czas', 'Energia wytworzona dzisiaj(kWh)']]
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
nowy_plik_fv.rename(columns={'Zaktualizowany czas':'Data'}, inplace=True)
nowy_plik_fv = nowy_plik_fv.resample('H', on='Data').Przyrost.sum()

nowy_plik_tauron = plik_tauron_godzinowe()[['Zaktualizowany czas', 'Dzień tygodnia', 'Pobór energii [kWh]', 'Oddanie [kWh]']]
nowy_plik_tauron.rename(columns={'Zaktualizowany czas':'Data'}, inplace=True)

# --------- testowy zapis plików -----------------
#nowy_plik_fv.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/plik_docelowy_fv.xlsx')
#nowy_plik_tauron.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/plik_docelowy_tauron.xlsx')

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
db_godzinowe()
# -----------------------------------------------------------------------------------------------------------------

number_rows = len(nowy_plik.index)
plik_docelowy = input('Podaj ścieżkę zapisu informacji wyjściowych: ')+'\Dane godzinowe.xlsx'
writer = pd.ExcelWriter(plik_docelowy, engine='xlsxwriter')
workbook = writer.book
total_fmt = workbook.add_format({'align': 'right', 'num_format': '#,##0.00', 'bold': True, 'bottom':6})
total_fmt.set_bg_color('#808080')
total_fmt.set_font_color('white')
total_fmt.set_font_size(15)
nowy_plik.to_excel(writer, index=False, sheet_name='Raport godzinowy')
workbook = writer.book
worksheet = writer.sheets['Raport godzinowy']
worksheet.set_zoom(100)
worksheet.set_column('A:B', 20)
worksheet.set_column('C:H', 25)
for column in range(2, 7):
    cell_location = xl_rowcol_to_cell(number_rows+1, column)
    start_range = xl_rowcol_to_cell(1, column)
    end_range = xl_rowcol_to_cell(number_rows, column)
    formula = "=SUM({:s}:{:s})".format(start_range, end_range)
    worksheet.write_formula(cell_location, formula, total_fmt)
worksheet.write_string(number_rows+1, 1, "Suma: ",total_fmt)
writer.save()