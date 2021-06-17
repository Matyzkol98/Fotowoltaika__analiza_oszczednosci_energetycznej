using System;
using System.Collections.Generic;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using Fotowoltaika_Aplikacja.Classes;
using LiveCharts;
using LiveCharts.Wpf;
using Microsoft.Office.Interop.Excel;
using System.Windows.Threading;
using Fotowoltaika_Aplikacja.ViewModels;


namespace Fotowoltaika_Aplikacja.Views
{
    /// <summary>
    /// Interaction logic for Pokaz_wyniki.xaml
    /// </summary>
    public partial class Pokaz_wyniki : UserControl
    {

       

        public Pokaz_wyniki()
        {
            InitializeComponent();
        }

        

        public static int przycisk_nacisniety_Pokz = 0;

        private void Btn_Clicked_Zaladuj(object sender, RoutedEventArgs e)
        {
            przycisk_nacisniety_Pokz = 1;
            
        }

        private void Btn_Click_Rysuj(object sender, RoutedEventArgs e)
        {
            przycisk_nacisniety_Pokz = 2;
        }

        

    }
}