using System;
using System.Collections.Generic;
using Microsoft.Win32;
using System.Windows;
using System.Data.SQLite;
using System.Data;
using Fotowoltaika_Aplikacja.Views;
using System.Diagnostics;
using Fotowoltaika_Aplikacja.ViewModels;
using Excel = Microsoft.Office.Interop.Excel;
using System.Windows.Controls;

namespace Fotowoltaika_Aplikacja.Classes
{
    public abstract class Obsluga_Interfejsu
    {
        // Metody - obsługa przycisków //
        

        public static void otworz_open_dialog()
        {
            if (Okno_wyboru_sciezki.przycisk_nacisniety_Ok == 1)
            {
                


               var dialog = new Ookii.Dialogs.Wpf.VistaFolderBrowserDialog();

                dialog.Description = "Wybierz sciezke folderu danych";
                dialog.UseDescriptionForTitle = true;
                dialog.ShowNewFolderButton = true;

                var result = dialog.ShowDialog();
                if(result == true)
                {
                    string Sciezka = dialog.SelectedPath;
                }

            }
            else if (Okno_wyboru_sciezki.przycisk_nacisniety_Ok == 2)
            { }
            else if (Okno_wyboru_sciezki.przycisk_nacisniety_Ok == 3)
            {
                var dialog = new Ookii.Dialogs.Wpf.VistaFolderBrowserDialog();

                dialog.Description = "Wybierz sciezke folderu danych wyjsciowych";
                dialog.UseDescriptionForTitle = true;
                dialog.ShowNewFolderButton = true;

                var result = dialog.ShowDialog();
                if (result == true)
                {
                     string Syg_Wyj = dialog.SelectedPath;
                }
            }
            else
            {

            }
        }

        public static void zaladuj_z_bazy_do_datagrid()
        
        {

            if (Glowny_Widok.przycisk_nacisniety == 2)    // Dla dobowych
            {

                
                var con = new SQLiteConnection("Data Source=c:\\Users\\user\\Documents\\Pliki_Testowe_Excel_I_Python\\Folder danych\\Danedobowe.sqlite;");
                try
                {
                    con.Open();
                    SQLiteCommand cmd = con.CreateCommand();
                    if (con.State == ConnectionState.Open)
                    {
                        // SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'; 

                        cmd.CommandText = "SELECT * FROM [C:/Users/user/Documents/Pliki_Testowe_Excel_I_Python/Folder danych/Danedobowe.db]";
                        using (SQLiteDataAdapter dataAdapter = new SQLiteDataAdapter(cmd.CommandText, con))
                        {
                            DataTable Wypelnij_danymi = new DataTable();
                            dataAdapter.Fill(Wypelnij_danymi);
                            Debug.WriteLine(Wypelnij_danymi);

                            //Pokaz_wyniki.DataGrid1.ItemsSource = dataTable.AsDataView();

                        }
                    }
                    else
                    { 
                        Debug.WriteLine("Zamkniete polaczenie"); 
                    }

                }
                catch (Exception exp)
                {
                    MessageBox.Show(exp.Message);

                    
                    OpenFileDialog openfile = new OpenFileDialog();
                    openfile.DefaultExt = ".xlsx";
                    openfile.Filter = "(.xlsx)|*.xlsx";
                    //openfile.ShowDialog();

                    var wyszukanyplik = openfile.ShowDialog();

                    if (wyszukanyplik == true)
                    {
                        //txtFilePath.Text = openfile.FileName;
                        string Text111 = openfile.FileName;
                        Microsoft.Office.Interop.Excel.Application excelApp = new Microsoft.Office.Interop.Excel.Application();
                        
                        Microsoft.Office.Interop.Excel.Workbook excelBook = excelApp.Workbooks.Open(Text111, 0, true, 5, "", "", true, Microsoft.Office.Interop.Excel.XlPlatform.xlWindows, "\t", false, false, 0, true, 1, 0);
                        Microsoft.Office.Interop.Excel.Worksheet excelSheet = (Microsoft.Office.Interop.Excel.Worksheet)excelBook.Worksheets.get_Item(1); ;
                        Microsoft.Office.Interop.Excel.Range excelRange = excelSheet.UsedRange;

                        string strCellData = "";
                        double douCellData;
                        int rowCnt = 0;
                        int colCnt = 0;

                        DataTable dt = new DataTable();
                        for (colCnt = 1; colCnt <= excelRange.Columns.Count; colCnt++)
                        {
                            string strColumn = "";
                            strColumn = (string)(excelRange.Cells[1, colCnt] as Microsoft.Office.Interop.Excel.Range).Value2;
                            dt.Columns.Add(strColumn, typeof(string));
                        }

                        for (rowCnt = 2; rowCnt <= excelRange.Rows.Count; rowCnt++)
                        {
                            string strData = "";
                            for (colCnt = 1; colCnt <= excelRange.Columns.Count; colCnt++)
                            {
                                try
                                {
                                    strCellData = (string)(excelRange.Cells[rowCnt, colCnt] as Microsoft.Office.Interop.Excel.Range).Value2;
                                    strData += strCellData + "|";
                                }
                                catch (Exception ex)
                                {
                                    douCellData = (excelRange.Cells[rowCnt, colCnt] as Microsoft.Office.Interop.Excel.Range).Value2;
                                    strData += douCellData.ToString() + "|";
                                }
                            }
                            strData = strData.Remove(strData.Length - 1, 1);
                            dt.Rows.Add(strData.Split('|'));
                        }


                        
                        //DataGrid1.ItemsSource = dt.DefaultView;

                        excelBook.Close(true, null, null);
                        excelApp.Quit();
                    }
                }
            }
            
            else if (Glowny_Widok.przycisk_nacisniety == 1)   // dla godzinowych
            {
                
                var con = new SQLiteConnection("Data Source=c:\\Users\\user\\Documents\\Pliki_Testowe_Excel_I_Python\\Folder danych\\Danegodzinowe.sqlite;");               
                
                try
                {
                    con.Open();
                    SQLiteCommand cmd = con.CreateCommand();
                        if (con.State == ConnectionState.Open)
                        {

                            cmd.CommandText = "SELECT * FROM DaneG";
                            using (SQLiteDataAdapter dataAdapter = new SQLiteDataAdapter(cmd.CommandText, con))
                            {
                                DataTable Wypelnij_danymi = new DataTable();
                                dataAdapter.Fill(Wypelnij_danymi);
                                Debug.WriteLine(Wypelnij_danymi);

                                //Pokaz_wyniki.DataGrid1.ItemsSource = dataTable.AsDataView();

                            }
                        }
                        else 
                        {
                        Debug.WriteLine("Zamkniete polaczenie");
                        }

                }
                catch (Exception exp)
                {
                    MessageBox.Show(exp.Message);
                }
            }
            else
            {
                Debug.WriteLine("Nie powiodło sie");
            }
            
        }

        public static void rysowanie_wykresu()
        {
            Debug.WriteLine("Dlaczego to się nie wykonuje?");
        }
    }
}
