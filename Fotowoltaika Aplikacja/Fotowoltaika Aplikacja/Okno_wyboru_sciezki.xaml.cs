using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Diagnostics; // potrzebne do uruchomienia cmd
using System.ComponentModel;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using Microsoft.Win32;

namespace Fotowoltaika_Aplikacja
{
    /// <summary>
    /// Interaction logic for Okno_wyboru_sciezki.xaml
    /// </summary>
    public partial class Okno_wyboru_sciezki : Window
    {
        public Okno_wyboru_sciezki()
        {
            InitializeComponent();
        }
        //_________________________ przyciski_okna_drugiego_________________________ //
        private void Przycisk_Powrot(object sender, RoutedEventArgs e)
        {
            MainWindow pierwsze_okno = new MainWindow();
            pierwsze_okno.Show();
            this.Close();
        }

        private void Przycisk_Dalej(object sender, RoutedEventArgs e)
        {
            string sciezka1 = TextBox1.Text;
            string sciezka2 = TextBox2.Text;
            string sciezka3 = TextBox3.Text;

            otworz_cmd(sciezka1, sciezka2, sciezka3);
            Pokaz_Wynik trzecie_okno = new Pokaz_Wynik();
            trzecie_okno.Show();
            this.Close();
        }


        private void wybor_sciezki_1_Button(object sender, RoutedEventArgs e)
        {
            OpenFileDialog okno_wyboru_pliku1 = new OpenFileDialog();
            okno_wyboru_pliku1.Filter = "Plik Excel (*.xlsx)|*.xlsx| Plik Excel (*.xls)|*.xls| All files (*.*)|*.*";
            okno_wyboru_pliku1.DefaultExt = ".xlsx";
            okno_wyboru_pliku1.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
            if (okno_wyboru_pliku1.ShowDialog() == true)
            {
                string nazwa_pliku1 = okno_wyboru_pliku1.FileName;
                TextBox1.Text = nazwa_pliku1;
            }
            else 
            {
                MessageBox.Show("Nie powiodla sie proba", "Blad", MessageBoxButton.OK, MessageBoxImage.Error);
            } 
            
        }
        private void wybor_sciezki_2_Button(object sender, RoutedEventArgs e)
        {
            OpenFileDialog okno_wyboru_pliku2 = new OpenFileDialog();
            okno_wyboru_pliku2.Filter = "Plik Excel (*.xlsx)|*.xlsx| Plik Excel (*.xls)|*.xls| All files (*.*)|*.*";
            okno_wyboru_pliku2.DefaultExt = ".xlsx";
            okno_wyboru_pliku2.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
            if (okno_wyboru_pliku2.ShowDialog() == true)
            {
                string nazwa_pliku2 = okno_wyboru_pliku2.FileName;
                TextBox2.Text = nazwa_pliku2;
            }
            else
            {
                MessageBox.Show("Nie powiodla sie proba", "Blad", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }
        private void wybor_sciezki_3_Button(object sender, RoutedEventArgs e)
        {
            OpenFileDialog okno_wyboru_folderu = new OpenFileDialog();
            okno_wyboru_folderu.Filter = "All files (*.*)|*.*";
            okno_wyboru_folderu.DefaultExt = "";
            okno_wyboru_folderu.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
            if (okno_wyboru_folderu.ShowDialog() == true)
            {
                string nazwa_pliku3 = okno_wyboru_folderu.FileName;
                TextBox3.Text = nazwa_pliku3;
            }
            else
            {
                MessageBox.Show("Nie powiodla sie proba", "Blad", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }
        /// _________________________Koniec Przycisków 2 okna_________________________ ///
        
        ///_________________________ Funkcje_________________________ ///

        // uruchomienie skryptu python 
        static void otworz_cmd(string sciezka1, string sciezka2, string sciezka3)
        {
            
            Process proc = new Process();
            proc.StartInfo.FileName = "cmd.exe";
            proc.StartInfo.WindowStyle = ProcessWindowStyle.Normal;
            proc.StartInfo.RedirectStandardInput = true;
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;

            proc.StartInfo.Arguments = @"/c  ""cd C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\ && python Dane_miesieczne.py""";
            //proc.StartInfo.Arguments = @"/c " + sciezka;

            //""C: \Users\user\Documents\Pliki_Testowe_Excel_I_Python\FalownikSF4ES008L9F256 - Statystyki dzienne - 20210317(1).xlsx && C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\dane(1).xlsx && C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\""
            proc.Start();

            proc.StandardInput.WriteLine(@"C: \Users\user\Documents\Pliki_Testowe_Excel_I_Python\FalownikSF4ES008L9F256 - Statystyki dzienne - 20210317(1).xlsx");
            proc.StandardInput.WriteLine(@"C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\dane (1).xlsx");
            proc.StandardInput.WriteLine(@"C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\");

            proc.WaitForExit();


        }

        

        ///_________________________ Koniec-Funkcje_________________________ ///
    }
}
