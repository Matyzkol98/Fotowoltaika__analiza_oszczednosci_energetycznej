# ------- Moduł konwertujacy pliki xlsx do plików db w bazie np. SQLite --------
import pandas as pd
import sqlite3
from CSV_to_XLSX import katalog, kolumna_0d

plik_1 = katalog+'/temp/plik_dla_DB.xlsx'
plik_2 = katalog+'/Dane dobowe.db'
plik_3 = katalog+'/temp/plik_dla_DB_godzinowy.xlsx'
plik_4 = katalog+'/Dane godzinowe.db'

class Xlsxtodb:
    def __init__(self, plik_1, plik_2, plik_3, plik_4):
        self.plik_1 = plik_1
        self.plik_2 = plik_2
        self.plik_3 = plik_3
        self.plik_4 = plik_4

    def db_dobowe():
        Nazwa_excel = plik_1
        Nazwa_db = plik_2
        xlsx = pd.read_excel(open(Nazwa_excel, 'rb'))
        xlsx.drop(kolumna_0d, axis=1, inplace=True)
        conn = sqlite3.connect(Nazwa_db)
        xlsx.to_sql(Nazwa_db, conn,  if_exists='replace', index=False)

    def db_godzinowe():
        Nazwa_excel = plik_3
        Nazwa_db = plik_4
        xlsx = pd.read_excel(open(Nazwa_excel, 'rb'))
        xlsx.drop(kolumna_0d, axis=1, inplace=True)
        conn = sqlite3.connect(Nazwa_db)
        xlsx.to_sql(Nazwa_db, conn,  if_exists='replace', index=False)
