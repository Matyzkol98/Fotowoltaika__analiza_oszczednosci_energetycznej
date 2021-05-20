using System.Windows.Input;
using Fotowoltaika_Aplikacja.Commands;
using Fotowoltaika_Aplikacja.Store;

namespace Fotowoltaika_Aplikacja.ViewModels
{
    public class Okno_wyboru_sciezki_model:ViewModelBase
    {
        public ICommand Command_PokazWynik
        {
            get;
        }

        public ICommand Command_GlownyWidok
        {
            get;
        }

        public Okno_wyboru_sciezki_model(NavigationStore navigationStore)
        {
            Command_PokazWynik = new Command_PokazWynik(navigationStore);
            Command_GlownyWidok = new Command_GlownyWidok(navigationStore);
        }

        // obsługa przycisków open dialog
        public ICommand Command_OtworzDialog
        {
            get;
        }

       
    }
}
