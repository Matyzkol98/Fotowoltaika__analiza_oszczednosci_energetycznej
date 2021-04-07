import pandas as pd
import numpy as np

# --------- moduł zmieniający znaki w pliku z Tauron z: ','->'.' i ';'->',' ---------

def zmiana_znakow_tauron_dobowe():
    sciezka_tauron = input('Podaj ścieżkę do pliku z Tauronu: ')
#    with open('C:/Users/KolodTad/Desktop/Fotovolt/Dobowe/dane.csv', 'rt') as file:
    with open(sciezka_tauron, 'rt') as file:
        with open('C:/Users/KolodTad/Desktop/Fotovolt/temp/dane_temp_dobowe.csv', 'wt') as file2:
            for line in file:
                file2.write(line.replace(',', '.'))
    with open('C:/Users/KolodTad/Desktop/Fotovolt/temp/dane_temp_dobowe.csv', 'rt') as file2:
        with open('C:/Users/KolodTad/Desktop/Fotovolt/temp/Tauron_temp_dobowe.csv', 'wt') as file:
            for line in file2:
                file.write(line.replace(';', ','))

def zmiana_znakow_tauron_godzinowe():
    with open('C:/Users/KolodTad/Desktop/Fotovolt/Godzinowe/dane.csv', 'rt') as file:
        with open('C:/Users/KolodTad/Desktop/Fotovolt/temp/dane_temp_godzinowe.csv', 'wt') as file2:
            for line in file:
                file2.write(line.replace(',', '.'))
    with open('C:/Users/KolodTad/Desktop/Fotovolt/temp/dane_temp_godzinowe.csv', 'rt') as file2:
        with open('C:/Users/KolodTad/Desktop/Fotovolt/temp/Tauron_temp_godzinowe.csv', 'wt') as file:
            for line in file2:
                file.write(line.replace(';', ','))

# --------- moduł zmieniający znaki w pliku z Tauron z: ','->'.' i ';'->',' ---------
def zmiana_csv_xlsx_dobowe():
    read_file = pd.read_csv('C:/Users/KolodTad/Desktop/Fotovolt/temp/Tauron_temp_dobowe.csv')
    read_file.rename(columns={'Unnamed: 0':'Zaktualizowany czas', 'Pob�r energii [kWh]':'Pobór energii [kWh]', 'Oddanie [kWh]':'Oddanie [kWh]', 'Unnamed: 3':''}, inplace=True)
    read_file.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/temp/Tauron_temp_dobowe.xlsx', index=None, header=True)

def zmiana_csv_xlsx_godzinowe():
    read_file = pd.read_csv('C:/Users/KolodTad/Desktop/Fotovolt/temp/Tauron_temp_godzinowe.csv')
    read_file.rename(columns={'Data. godzina':'Zaktualizowany czas', 'Pob�r energii [kWh]':'Pobór energii [kWh]', 'Oddanie [kWh]':'Oddanie [kWh]', 'Unnamed: 3':''}, inplace=True)
    read_file.to_excel('C:/Users/KolodTad/Desktop/Fotovolt/temp/Tauron_temp_godzinowe.xlsx', index=None, header=True)