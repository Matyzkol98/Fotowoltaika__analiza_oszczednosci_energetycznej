import pandas as pd

def plik_fotowoltaika_dobowe():
    sciezka_fv = input('Podaj ścieżkę do pliku z falownika: ')
    plik_fv = pd.read_excel(sciezka_fv, parse_dates=['Zaktualizowany czas'])
#    plik_fv = pd.read_excel('C:/Users/KolodTad/Desktop/Fotovolt/Dobowe/FalownikSF4ES008L9F256-Statystyki dzienne-20210406.xlsx', parse_dates=['Zaktualizowany czas'])
    plik_fv['Zaktualizowany czas'] = pd.to_datetime(plik_fv['Zaktualizowany czas']).dt.date
    plik_fv['Dzień tygodnia'] = pd.to_datetime(plik_fv['Zaktualizowany czas']).dt.day_name()
    plik_fv.head()
    return plik_fv

def plik_fotowoltaika_godzinowe():
#    sciezka_fv = input('Podaj ścieżkę do pliku z falownika: ')
#    plik_fv = pd.read_excel(sciezka_fv, parse_dates=['Zaktualizowany czas'])
    plik_fv = pd.read_excel('C:/Users/KolodTad/Desktop/Fotovolt/Godzinowe/Falownik.xlsx', parse_dates=['Zaktualizowany czas'])
    plik_fv['Zaktualizowany czas'] = pd.to_datetime(plik_fv['Zaktualizowany czas']).dt.date
    plik_fv['Dzień tygodnia'] = pd.to_datetime(plik_fv['Zaktualizowany czas']).dt.day_name()
    plik_fv.head()
    return plik_fv