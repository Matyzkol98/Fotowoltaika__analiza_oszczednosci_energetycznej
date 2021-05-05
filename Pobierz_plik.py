from CSV_to_XLSX import *             # można wypisywać np. Csvtoxlsx, sdsd, wpisywanie poszczegółnych klas, lub zmiennych

nazwa_pliku_fv = input('Podaj nazwę pliku z falownika fotowoltaiki: ')
plik_1 = katalog + '/Dobowe/' + nazwa_pliku_fv + '.xlsx'
plik_2 = katalog + '/Godzinowe/' + nazwa_pliku_fv + '.xlsx'
kolunma = 'Zaktualizowany czas'

class Plikfotowoltaika:
    def __init__(self, plik_1, plik_2, kolumna):
        self.plik_1 = plik_1
        self.plik_2 = plik_2
        self.kolunma = kolumna

    def plik_fotowoltaika_dobowe():
        plik_fv = pd.read_excel(plik_1, parse_dates=[kolunma])
        plik_fv.rename(columns={kolunma:'Data'}, inplace=True)
        plik_fv['Data'] = pd.to_datetime(plik_fv['Data']).dt.date
        plik_fv.head()
        return plik_fv

    def plik_fotowoltaika_godzinowe():
        plik_fv = pd.read_excel(plik_2, parse_dates=[kolunma])
        plik_fv.rename(columns={kolunma: 'Data'}, inplace=True)
        plik_fv['Data'] = pd.to_datetime(plik_fv['Data'])
        plik_fv['Data'] = plik_fv['Data'] + pd.Timedelta('3600000000000')    # przesunięcie godziny w przód
        plik_fv.head()
        return plik_fv

class Pliktauron:
    def plik_tauron_dobowe():
        Csvtoxlsx.zmiana_znakow_tauron_dobowe()
        Csvtoxlsx.zmiana_csv_xlsx_dobowe()
        plik_z_tauron = pd.read_excel(plik_4, parse_dates=['Data'])
        plik_z_tauron['Data'] = pd.to_datetime(plik_z_tauron['Data']).dt.date
        plik_z_tauron['Dzień tygodnia'] = pd.to_datetime(plik_z_tauron['Data']).dt.day_name()
        plik_z_tauron.head()
        return plik_z_tauron

    def plik_tauron_godzinowe():
        Csvtoxlsx.zmiana_znakow_tauron_godzinowe()
        Csvtoxlsx.zmiana_csv_xlsx_godzinowe()
        plik_z_tauron = pd.read_excel(plik_8, parse_dates=['Data'])
        plik_z_tauron['Data'] = pd.to_datetime(plik_z_tauron['Data'])
        plik_z_tauron['Dzień tygodnia'] = pd.to_datetime(plik_z_tauron['Data']).dt.day_name()
        plik_z_tauron.head()
        return plik_z_tauron