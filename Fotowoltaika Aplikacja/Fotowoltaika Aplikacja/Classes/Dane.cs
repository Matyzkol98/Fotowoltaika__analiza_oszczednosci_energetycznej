using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Diagnostics;
using System.ComponentModel;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Microsoft.Win32;

namespace Fotowoltaika_Aplikacja.Classes
{
    public class Dane
    {
        // funkcje
        public void otworz_open_dialog(object sender, RoutedEventArgs e)
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

        static void otworz_cmd(string sciezka1, string sciezka2, string sciezka3)
        {

            Process proc = new Process();
            proc.StartInfo.FileName = "cmd.exe";
            proc.StartInfo.WindowStyle = ProcessWindowStyle.Normal;
            proc.StartInfo.RedirectStandardInput = true;
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;

            proc.StartInfo.Arguments = @"/c  ""cd C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\Fot\Dane_dobowe.py""";
            //proc.StartInfo.Arguments = @"/c " + sciezka;

            //""C: \Users\user\Documents\Pliki_Testowe_Excel_I_Python\FalownikSF4ES008L9F256 - Statystyki dzienne - 20210317(1).xlsx && C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\dane(1).xlsx && C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\""
            proc.Start();

            //proc.StandardInput.WriteLine(@"C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\FalownikSF4ES008L9F256.xlsx");
            //proc.StandardInput.WriteLine(@"C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\dane.xlsx");
            proc.StandardInput.WriteLine(@"C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\");

            proc.WaitForExit();


        }
    }
}
