import pandas as pd
import sqlite3

def db_dobowe():
    Nazwa_excel = 'C:/Users/KolodTad/Desktop/Fotovolt/temp/plik_dla_DB.xlsx'
    Nazwa_db = 'C:/Users/KolodTad/Desktop/Fotovolt/Dane dobowe.db'
    xlsx = pd.read_excel(open(Nazwa_excel, 'rb'))
    conn = sqlite3.connect(Nazwa_db)
    xlsx.to_sql(Nazwa_db, conn,  if_exists='replace')

def db_godzinowe():
    Nazwa_excel = 'C:/Users/KolodTad/Desktop/Fotovolt/temp/plik_dla_DB_godzinowy.xlsx'
    Nazwa_db = 'C:/Users/KolodTad/Desktop/Fotovolt/Dane godzinowe.db'
    xlsx = pd.read_excel(open(Nazwa_excel, 'rb'))
    conn = sqlite3.connect(Nazwa_db)
    xlsx.to_sql(Nazwa_db, conn,  if_exists='replace')
