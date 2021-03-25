using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
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

namespace Fotowoltaika_Aplikacja
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()  
        {
            InitializeComponent();
        }
        // przyciski-obsługa
        private void przycisk_raport_dobowy(object sender, RoutedEventArgs e)
        {
        }

        private void przycisk_raport_miesieczny(object sender, RoutedEventArgs e)
        {
            Okno_wyboru_sciezki drugie_okno = new Okno_wyboru_sciezki();
            drugie_okno.Show();
            this.Close();
        }

        private void przycisk_raport_roczny(object sender, RoutedEventArgs e)
        {

        }

    }
}
