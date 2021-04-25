import pandas as pd
from datetime import datetime, timedelta

def plik_fotowoltaika_dobowe():
    sciezka_fv = input('Podaj ścieżkę do pliku z falownika: ')
    plik_fv = pd.read_excel(sciezka_fv, parse_dates=['Zaktualizowany czas'])
#    plik_fv = pd.read_excel('C:/Users/KolodTad/Desktop/Fotovolt/Dobowe/FalownikSF4ES008L9F256-Statystyki dzienne-20210406.xlsx', parse_dates=['Zaktualizowany czas'])
    plik_fv['Zaktualizowany czas'] = pd.to_datetime(plik_fv['Zaktualizowany czas']).dt.date
#    plik_fv['Dzień tygodnia'] = pd.to_datetime(plik_fv['Zaktualizowany czas']).dt.day_name()
    plik_fv.head()
    return plik_fv

def plik_fotowoltaika_godzinowe():
    sciezka_fv = input('Podaj ścieżkę do pliku z falownika: ')
    plik_fv = pd.read_excel(sciezka_fv, parse_dates=['Zaktualizowany czas'])
#    plik_fv = pd.read_excel('C:/Users/KolodTad/Desktop/Fotovolt/Godzinowe/FalownikSF4ES008L9F256-Szczegółowe dane-20210421.xlsx', parse_dates=['Zaktualizowany czas'])
#    plik_fv['Godzina'] = pd.to_datetime(plik_fv['Zaktualizowany czas']).dt.date
    plik_fv['Zaktualizowany czas'] = pd.to_datetime(plik_fv['Zaktualizowany czas'])
#    plik_fv['Dzień tygodnia'] = pd.to_datetime(plik_fv['Zaktualizowany czas']).dt.day_name()
    plik_fv['Zaktualizowany czas'] = plik_fv['Zaktualizowany czas'] + pd.Timedelta('3600000000000')    # przesunięcie godziny w przód
    plik_fv.head()
    return plik_fv