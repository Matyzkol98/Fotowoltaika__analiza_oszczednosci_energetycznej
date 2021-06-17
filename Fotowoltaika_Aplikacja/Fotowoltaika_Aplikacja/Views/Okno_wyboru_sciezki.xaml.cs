using System;
using System.Collections.Generic;
using System.Text;
using System.Windows.Input;
using System.Windows.Controls;
using Fotowoltaika_Aplikacja.ViewModels;
using Fotowoltaika_Aplikacja.Views;
using Fotowoltaika_Aplikacja.Store;
using Fotowoltaika_Aplikacja.Classes;

namespace Fotowoltaika_Aplikacja.Views
{
    /// <summary>
    /// Interaction logic for Okno_wyboru_sciezki.xaml
    /// </summary>
    public partial class Okno_wyboru_sciezki : UserControl
    {
        public Okno_wyboru_sciezki()
        {
            InitializeComponent();
        }

        public static int przycisk_nacisniety_Ok = 0;

        private void Btn_Clicked_1(object sender, System.Windows.RoutedEventArgs e)
        {
            przycisk_nacisniety_Ok = 1;
        }

        private void Btn_Clicked_2(object sender, System.Windows.RoutedEventArgs e)
        {
            przycisk_nacisniety_Ok = 2;
        }

        private void Btn_Clicked_3(object sender, System.Windows.RoutedEventArgs e)
        {
            przycisk_nacisniety_Ok = 3;
        }

        private void Uruchom_Clicked(object sender, System.Windows.RoutedEventArgs e)
        {
            Dane.otworz_cmd();
        }
    }
}
