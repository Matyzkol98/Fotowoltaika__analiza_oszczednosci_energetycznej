# --------- import modułów ---------
from xlsxwriter.utility import xl_rowcol_to_cell
import pandas as pd
import numpy as np
from Pobierz_plik_fv import plik_fotowoltaika_dobowe
from Pobierz_plik_tauron import plik_tauron_dobowe
from XLSX_to_DB import db_dobowe

# --------- przekształcenia plików wsadowych z pobraniem plików z Falownika i Tauron ---------
nowy_plik_fv = plik_fotowoltaika_dobowe()[['Zaktualizowany czas', 'Produkcja(kWh)']]
nowy_plik_fv.rename(columns={'Zaktualizowany czas':'Data'}, inplace=True)
nowy_plik_tauron = plik_tauron_dobowe()[['Zaktualizowany czas', 'Dzień tygodnia', 'Pobór energii [kWh]', 'Oddanie [kWh]']]
nowy_plik_tauron.rename(columns={'Zaktualizowany czas':'Data'}, inplace=True)
print(nowy_plik_tauron)

#nowy_plik_fv.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/plik_docelowy_fv.xlsx')
#nowy_plik_tauron.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/plik_docelowy_tauron.xlsx')

# --------- sklejenie plików w nowy plik ---------
right = pd.DataFrame(nowy_plik_fv)
left = pd.DataFrame(nowy_plik_tauron)
nowy_plik = pd.merge(left, right, on='Data')

# --------- utworzenie nowych kolumn ---------
nowy_plik['Zużytkowano z FV [kWh]'] = np.float_()   # NaN - trzeba było zamienic na typ float dla tych kolumn
nowy_plik['Zużycie dom [kWh]'] = np.float_()        # inaczej kolumny poniżej się nie liczyły matematycznie

# --------- zaindeksowanie kolumn do operacji matematycznych ---------
index_produkcja = nowy_plik.columns.get_loc('Produkcja(kWh)')
index_oddanie = nowy_plik.columns.get_loc('Oddanie [kWh]')
index_pobor = nowy_plik.columns.get_loc('Pobór energii [kWh]')
index_total = nowy_plik.columns.get_loc('Zużytkowano z FV [kWh]')
index_zuzycie = nowy_plik.columns.get_loc('Zużycie dom [kWh]')

# --------- operacje matematyczne - wyliczania dla nowych kolumn ---------
for row in range(0, len(nowy_plik)):
    nowy_plik.iat[row, index_total] = nowy_plik.iat[row, index_produkcja] - nowy_plik.iat[row, index_oddanie]
    nowy_plik.iat[row, index_zuzycie] = nowy_plik.iat[row, index_total] + nowy_plik.iat[row, index_pobor]

# --------- kolorowanie wierszy ---------
def positive_max(s):
    is_max = s == s.max()
    return ['background-color: green' if v else '' for v in is_max]
def negative_max(s):
    is_max = s == s.max()
    return ['background-color: red' if v else '' for v in is_max]
def middle_max(s):
    is_max = s == s.max()
    return ['background-color: yellow' if v else '' for v in is_max]

t = range(0, len(nowy_plik)-1)
nowy_plik = nowy_plik.style\
               .apply(positive_max, subset=pd.IndexSlice[t, ['Produkcja(kWh)']])\
               .apply(positive_max, subset=pd.IndexSlice[:, ['Produkcja(kWh)']])\
               .apply(negative_max, subset=pd.IndexSlice[t, ['Pobór energii [kWh]','Zużycie dom [kWh]']])\
               .apply(negative_max, subset=pd.IndexSlice[:, ['Pobór energii [kWh]','Zużycie dom [kWh]']])\
               .apply(middle_max, subset=pd.IndexSlice[t, ['Oddanie [kWh]','Zużytkowano z FV [kWh]']])\
               .apply(middle_max, subset=pd.IndexSlice[:, ['Oddanie [kWh]','Zużytkowano z FV [kWh]']])#\
               #.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/temp/plik_dla_DB.xlsx')

# ------------ tworzenia pliku DB -------------
sql_plik = nowy_plik
sql_plik.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/temp/plik_dla_DB.xlsx')
db_dobowe()
# -----------------------------------------------------------------------------------------------------------------

number_rows = len(nowy_plik.index)
plik_docelowy = input('Podaj ścieżkę zapisu informacji wyjściowych: ')+'\Dane dobowe.xlsx'
writer = pd.ExcelWriter(plik_docelowy, engine='xlsxwriter')
workbook = writer.book
total_fmt = workbook.add_format({'align': 'right', 'num_format': '#,##0.00', 'bold': True, 'bottom':6})
total_fmt.set_bg_color('#808080')
total_fmt.set_font_color('white')
total_fmt.set_font_size(15)
nowy_plik.to_excel(writer, index=False, sheet_name='Raport dobowy')
workbook = writer.book
worksheet = writer.sheets['Raport dobowy']
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


