using System;
using System.Diagnostics;
using System.Windows;
using Microsoft.Win32;

namespace Fotowoltaika_Aplikacja.Classes
{
    public class Dane
    {


        // metody //
        

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
