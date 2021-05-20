using System;
using System.Collections.Generic;
using Microsoft.Win32;
using System.Windows;
using System.Data.SQLite;
using System.Data;
using System.Configuration;
using Dapper;

namespace Fotowoltaika_Aplikacja.Classes
{
    public abstract class Obsluga_Interfejsu
    {
        // Metody - obsługa przycisków //
        public static void otworz_open_dialog()
        {
            OpenFileDialog okno_wyboru_pliku1 = new OpenFileDialog();
            okno_wyboru_pliku1.Filter = "Plik Excel (*.xlsx)|*.xlsx| Plik Excel (*.xls)|*.xls| All files (*.*)|*.*";
            okno_wyboru_pliku1.DefaultExt = ".xlsx";
            okno_wyboru_pliku1.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
            if (okno_wyboru_pliku1.ShowDialog() == true)
            {
                string nazwa_pliku1 = okno_wyboru_pliku1.FileName;
                //TextBox1.Text = nazwa_pliku1;
            }
            else
            {
                MessageBox.Show("Nie powiodla sie proba", "Blad", MessageBoxButton.OK, MessageBoxImage.Error);
            }

        }

        public static void zaladuj_z_bazy_do_datagrid()
        {
                 
        }

        /*public static List<Dane_dobowe> zaladuj_dane()
        {
            using (IDbConnection conn = new SQLiteConnection(LoadConnectionString()))
            {
                var output = conn.Query<Dane>("select * from C:/Users/KolodTad/Desktop/Fotovolt/Dane dobowe.db", new DynamicParameters());
                return output.ToList();
            }
        }

        private static string LoadConnectionString(string id = "Default")
        {
            return ConfigurationManager.ConnectionStrings[id].ConnectionString;

        }*/
        public static void rysowanie_wykresu()
        {

        }
    }
}
