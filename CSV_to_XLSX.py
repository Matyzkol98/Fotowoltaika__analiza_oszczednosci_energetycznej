# --------- moduł zmieniający znaki w pliku z Tauron z: ','->'.' i ';'->',' ---------

import pandas as pd

katalog = input('Podaj ścieżkę do katalogu z danymi: ').replace('\\', '/')
plik_1 = katalog+'/Dobowe/dane.csv'
plik_2 = katalog+'/temp/dane_temp_dobowe.csv'
plik_3 = katalog+'/temp/Tauron_temp_dobowe.csv'
plik_4 = katalog+'/temp/Tauron_temp_dobowe.xlsx'
plik_5 = katalog+'/Godzinowe/dane.csv'
plik_6 = katalog+'/temp/dane_temp_godzinowe.csv'
plik_7 = katalog+'/temp/Tauron_temp_godzinowe.csv'
plik_8 = katalog+'/temp/Tauron_temp_godzinowe.xlsx'
kolumna_0d = 'Unnamed: 0'
kolumna_0g = 'Data. godzina'
kolumna_1 = 'Pob�r energii [kWh]'
kolumna_2 = 'Oddanie [kWh]'
kolumna_3 = 'Unnamed: 3'

class Csvtoxlsx:
    def __init__(self, katalog, plik_1, plik_2, plik_3, plik_4,
                                    plik_5, plik_6, plik_7, plik_8,
                                        kolumna_0d, kolumna_0g, kolumna_1, kolumna_2, kolumna_3):
        self.katalog = katalog
        self.plik_1 = plik_1
        self.plik_2 = plik_2
        self.plik_3 = plik_3
        self.plik_4 = plik_4
        self.plik_5 = plik_5
        self.plik_6 = plik_6
        self.plik_7 = plik_7
        self.plik_8 = plik_8
        self.kolumna_0d = kolumna_0d
        self.kolumna_0g = kolumna_0g
        self.kolumna_1 = kolumna_1
        self.kolumna_2 = kolumna_2
        self.kolumna_3 = kolumna_3

# Zastosowano poniższą metodę z pętlą for dlatego, że plik z Tauron jest specyficznym plikiem csv i pandas go nie odczytuje
    def zmiana_znakow_tauron_dobowe():
        with open(plik_1, 'rt') as file:
            with open(plik_2, 'wt') as file2:
                for line in file:
                    file2.write(line.replace(',', '.'))
        with open(plik_2, 'rt') as file2:
            with open(plik_3, 'wt') as file:
                for line in file2:
                    file.write(line.replace(';', ','))

    def zmiana_znakow_tauron_godzinowe():
        with open(plik_5, 'rt') as file:
            with open(plik_6, 'wt') as file2:
                for line in file:
                    file2.write(line.replace(',', '.'))
        with open(plik_6, 'rt') as file2:
            with open(plik_7, 'wt') as file:
                for line in file2:
                    file.write(line.replace(';', ','))

# --------- moduł zmieniający nazwy kolumn w pliku z Tauron ---------
    def zmiana_csv_xlsx_dobowe():
        read_file = pd.read_csv(plik_3)
        read_file.rename(columns={kolumna_0d:'Data', kolumna_1:'Pobór energii [kWh]',
                                  kolumna_2:'Oddanie [kWh]'}, inplace=True)
        read_file.drop(kolumna_3, axis=1, inplace=True)
        read_file.to_excel(plik_4, index=None, header=True)

    def zmiana_csv_xlsx_godzinowe():
        read_file = pd.read_csv(plik_7)
        read_file.rename(columns={kolumna_0g: 'Data', kolumna_1: 'Pobór energii [kWh]',
                                  kolumna_2: 'Oddanie [kWh]'}, inplace=True)
        read_file.drop(kolumna_3, axis=1, inplace=True)
        read_file.to_excel(plik_8, index=None, header=True)
