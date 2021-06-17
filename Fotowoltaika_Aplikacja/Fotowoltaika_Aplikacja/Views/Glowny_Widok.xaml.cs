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
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Fotowoltaika_Aplikacja.Views
{
    /// <summary>
    /// Interaction logic for Glowny_Widok.xaml
    /// </summary>
    public partial class Glowny_Widok : UserControl
    {
        public Glowny_Widok()
        {
            InitializeComponent();
        }

        public static int przycisk_nacisniety = 0;
        

        private void Przycisk_godz(object sender, RoutedEventArgs e)
        {
            przycisk_nacisniety = 1;
        }

        private void Przycisk_dob(object sender, RoutedEventArgs e)
        {
            przycisk_nacisniety = 2;
        }
    }
}
