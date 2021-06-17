using System;
using System.Diagnostics;
using System.Windows;
using Microsoft.Win32;
using Fotowoltaika_Aplikacja.ViewModels;
using Fotowoltaika_Aplikacja.Views;

namespace Fotowoltaika_Aplikacja.Classes
{
    public class Dane
    {


        // metody //
        

        public static void otworz_cmd()
        {
            if (Glowny_Widok.przycisk_nacisniety == 2)
            {
                Process proc = new Process();
                proc.StartInfo.FileName = "cmd.exe";
                proc.StartInfo.WindowStyle = ProcessWindowStyle.Normal;
                proc.StartInfo.RedirectStandardInput = true;
                proc.StartInfo.RedirectStandardOutput = true;
                proc.StartInfo.UseShellExecute = false;

                proc.StartInfo.Arguments = @"/c  ""cd C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\Dane_dobowe.py""";
                //proc.StartInfo.Arguments = @"/c " + sciezka;

                //""C: \Users\user\Documents\Pliki_Testowe_Excel_I_Python\FalownikSF4ES008L9F256 - Statystyki dzienne - 20210317(1).xlsx && C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\dane(1).xlsx && C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\""
                proc.Start();

                //proc.StandardInput.WriteLine(@"C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\FalownikSF4ES008L9F256.xlsx");
                //proc.StandardInput.WriteLine(@"C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\dane.xlsx");
                proc.StandardInput.WriteLine(@"C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\Folderdanych");
                proc.StandardInput.WriteLine(@"Falownik");
                proc.StandardInput.WriteLine(@"C:\Users\user\Desktop");

                proc.WaitForExit();
            }
            else if (Glowny_Widok.przycisk_nacisniety == 1)
            {
                Process proc = new Process();
                proc.StartInfo.FileName = "cmd.exe";
                proc.StartInfo.WindowStyle = ProcessWindowStyle.Normal;
                proc.StartInfo.RedirectStandardInput = true;
                proc.StartInfo.RedirectStandardOutput = true;
                proc.StartInfo.UseShellExecute = false;

                proc.StartInfo.Arguments = @"/c  ""cd C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\Dane_godzinowe.py""";
                //proc.StartInfo.Arguments = @"/c " + sciezka;

                proc.Start();

                proc.StandardInput.WriteLine(@"C:\Users\user\Documents\Pliki_Testowe_Excel_I_Python\Folderdanych");
                proc.StandardInput.WriteLine(@"Falownik1");
                proc.StandardInput.WriteLine(@"C:\Users\user\Desktop");

                proc.WaitForExit();
            }
            else 
            { }

        }
    }
}
