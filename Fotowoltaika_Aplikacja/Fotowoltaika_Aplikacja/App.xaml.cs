using System.Windows;
using Fotowoltaika_Aplikacja.ViewModels;
using Fotowoltaika_Aplikacja.Store;


namespace Fotowoltaika_Aplikacja
{
    public partial class App : Application
    {
        protected override void OnStartup(StartupEventArgs e)
        {

            NavigationStore navigationStore = new NavigationStore();
            navigationStore.ObecnyWidokModel = new Glowny_widok_model(navigationStore);

            MainWindow = new MainWindow()
            {
                DataContext = new Main_Window_View_Model(navigationStore)
            };


            MainWindow.Show();

            base.OnStartup(e);

        }

    }
}
