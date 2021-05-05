# --------- kolorowanie max i min oraz sumowanie kolumn w Excel---------

import pandas as pd
from xlsxwriter.utility import xl_rowcol_to_cell

class Maxmin:
    def positive_max(s):
        is_max = s == s.max()
        return ['background-color: green' if v else '' for v in is_max]
    def negative_max(s):
        is_max = s == s.max()
        return ['background-color: red' if v else '' for v in is_max]
    def middle_max(s):
        is_max = s == s.max()
        return ['background-color: yellow' if v else '' for v in is_max]

def colormaxmin_sum_dobowy(plik):
    t = range(0, len(plik)-1)
    plik = plik.style\
                   .apply(Maxmin.positive_max, subset=pd.IndexSlice[t, ['Produkcja(kWh)']])\
                   .apply(Maxmin.positive_max, subset=pd.IndexSlice[:, ['Produkcja(kWh)']])\
                   .apply(Maxmin.negative_max, subset=pd.IndexSlice[t, ['Pobór energii [kWh]','Zużycie dom [kWh]']])\
                   .apply(Maxmin.negative_max, subset=pd.IndexSlice[:, ['Pobór energii [kWh]','Zużycie dom [kWh]']])\
                   .apply(Maxmin.middle_max, subset=pd.IndexSlice[t, ['Oddanie [kWh]','Zużytkowano z FV [kWh]']])\
                   .apply(Maxmin.middle_max, subset=pd.IndexSlice[:, ['Oddanie [kWh]','Zużytkowano z FV [kWh]']])
    number_rows = len(plik.index)
    plik_docelowy = input('Podaj ścieżkę zapisu informacji wyjściowych: ')+'\Dane dobowe.xlsx'
    writer = pd.ExcelWriter(plik_docelowy, engine='xlsxwriter')
    workbook = writer.book
    total_fmt = workbook.add_format({'align': 'right', 'num_format': '#,##0.00', 'bold': True, 'bottom':6})
    total_fmt.set_bg_color('#808080')
    total_fmt.set_font_color('white')
    total_fmt.set_font_size(15)
    plik.to_excel(writer, index=False, sheet_name='Raport dobowy')
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
    return plik

def colormaxmin_sum_godzinowy(plik):
    number_rows = len(plik.index)
    plik_docelowy = input('Podaj ścieżkę zapisu informacji wyjściowych: ')+'\Dane godzinowe.xlsx'
    writer = pd.ExcelWriter(plik_docelowy, engine='xlsxwriter')
    workbook = writer.book
    total_fmt = workbook.add_format({'align': 'right', 'num_format': '#,##0.00', 'bold': True, 'bottom':6})
    total_fmt.set_bg_color('#808080')
    total_fmt.set_font_color('white')
    total_fmt.set_font_size(15)
    plik.to_excel(writer, index=False, sheet_name='Raport godzinowy')
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
    return plik