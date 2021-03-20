# --------- import modułów ---------
from IPython.display import display
from xlsxwriter.utility import xl_rowcol_to_cell
import pandas as pd
import numpy as np
import openpyxl
import datetime


# --------- pobieranie pliku z falownika ---------
sciezka_fv = input('Podaj ścieżkę do pliku z falownika: ')
plik_fv = pd.read_excel(sciezka_fv, parse_dates=['Zaktualizowany czas'])
plik_fv['Zaktualizowany czas'] = pd.to_datetime(plik_fv['Zaktualizowany czas']).dt.date
plik_fv['Dzień tygodnia'] = pd.to_datetime(plik_fv['Zaktualizowany czas']).dt.day_name()
plik_fv.head()

# --------- pobieranie pliku z Tauron ---------
sciezka_tauron = input('Podaj ścieżkę do pliku z Tauronu: ')
plik_tauron = pd.read_excel(sciezka_tauron, parse_dates=['Zaktualizowany czas'])
plik_tauron['Zaktualizowany czas'] = pd.to_datetime(plik_tauron['Zaktualizowany czas']).dt.date
plik_tauron.head()

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
#nowy_plik.loc['Suma:'] = nowy_plik.select_dtypes(pd.np.number).sum()

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

#nowy_plik.loc['Suma:'] = pd.Series(nowy_plik['Zużytkowano z FV [kWh]'].sum(), index = ['Zużytkowano z FV [kWh]'])
#nowy_plik.loc['Suma:'] = nowy_plik.select_dtypes(pd.np.number).sum()

t = range(0, len(nowy_plik)-1)
nowy_plik = nowy_plik.style\
               .apply(positive_max, subset=pd.IndexSlice[t, ['Produkcja(kWh)']])\
               .apply(positive_max, subset=pd.IndexSlice[:, ['Produkcja(kWh)']])\
               .apply(negative_max, subset=pd.IndexSlice[t, ['Pobór energii [kWh]','Zużycie dom [kWh]']])\
               .apply(negative_max, subset=pd.IndexSlice[:, ['Pobór energii [kWh]','Zużycie dom [kWh]']])\
               .apply(middle_max, subset=pd.IndexSlice[t, ['Generacja [kWh]','Zużytkowano z FV [kWh]']])\
               .apply(middle_max, subset=pd.IndexSlice[:, ['Generacja [kWh]','Zużytkowano z FV [kWh]']])#\
#               .to_excel('C:/Users/KolodTad/Desktop/Fotovolt/plik_docelowy.xlsx')

#display(nowy_plik)

number_rows = len(nowy_plik.index)
plik_docelowy = input('Podaj ścieżkę zapisu informacji wyjściowych: ')+'Plik docelowy.xlsx'
writer = pd.ExcelWriter(plik_docelowy, engine='xlsxwriter')
workbook = writer.book
total_fmt = workbook.add_format({'align': 'right', 'num_format': '#,##0.00', 'bold': True, 'bottom':6})
total_fmt.set_bg_color('#808080')
total_fmt.set_font_color('white')
total_fmt.set_font_size(15)
nowy_plik.to_excel(writer, index=False, sheet_name='Raport miesięczny')
workbook = writer.book
worksheet = writer.sheets['Raport miesięczny']
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

# --------- zapis do nowego pliku zagregowanych danych ---------
#nowy_plik.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/plik_docelowy.xlsx')