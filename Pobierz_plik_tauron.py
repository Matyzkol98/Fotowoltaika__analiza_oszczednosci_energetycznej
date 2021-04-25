import pandas as pd
import CSV_to_XLSX

def plik_tauron_dobowe():
    CSV_to_XLSX.zmiana_znakow_tauron_dobowe()
    CSV_to_XLSX.zmiana_csv_xlsx_dobowe()
    plik_z_tauron = pd.read_excel('C:/Users/KolodTad/Desktop/Fotovolt/temp/Tauron_temp_dobowe.xlsx', parse_dates=['Zaktualizowany czas'])
    plik_z_tauron['Zaktualizowany czas'] = pd.to_datetime(plik_z_tauron['Zaktualizowany czas']).dt.date
    plik_z_tauron['Dzień tygodnia'] = pd.to_datetime(plik_z_tauron['Zaktualizowany czas']).dt.day_name()
    plik_z_tauron.head()
    return plik_z_tauron

def plik_tauron_godzinowe():
    CSV_to_XLSX.zmiana_znakow_tauron_godzinowe()
    CSV_to_XLSX.zmiana_csv_xlsx_godzinowe()
    plik_z_tauron = pd.read_excel('C:/Users/KolodTad/Desktop/Fotovolt/temp/Tauron_temp_godzinowe.xlsx', parse_dates=['Zaktualizowany czas'])
    plik_z_tauron['Zaktualizowany czas'] = pd.to_datetime(plik_z_tauron['Zaktualizowany czas'])
    plik_z_tauron['Dzień tygodnia'] = pd.to_datetime(plik_z_tauron['Zaktualizowany czas']).dt.day_name()
    plik_z_tauron.head()
    return plik_z_tauron