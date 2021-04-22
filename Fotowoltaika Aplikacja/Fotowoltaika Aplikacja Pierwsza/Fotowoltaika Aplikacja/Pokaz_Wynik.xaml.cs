using System;
using System.Collections.Generic;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace Fotowoltaika_Aplikacja
{
    /// <summary>
    /// Interaction logic for Pokaz_Wynik.xaml
    /// </summary>
    public partial class Pokaz_Wynik : Window
    {
        public Pokaz_Wynik()
        {
            InitializeComponent();
        }




        private void Powrot2_Button(object sender, RoutedEventArgs e)
        {
            Okno_wyboru_sciezki drugie_okno2 = new Okno_wyboru_sciezki();
            drugie_okno2.Show();
            this.Close();
        }

        private void Stworz_Wykres_Button(object sender, RoutedEventArgs e)
        {

        }

        private void Zaladuj_Plik_Button(object sender, RoutedEventArgs e)
        {

        }
    }
}
