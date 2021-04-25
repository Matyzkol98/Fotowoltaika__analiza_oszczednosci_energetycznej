using Fotowoltaika_Aplikacja.Commands;
using Fotowoltaika_Aplikacja.Store;
using System.Windows.Input;

namespace Fotowoltaika_Aplikacja.ViewModels
{
    public class Glowny_widok_model : ViewModelBase
    { 
       public ICommand Command_OknoWyboruSciezki 
        { 
            get;
        }
       
       public Glowny_widok_model(NavigationStore navigationStore)
        {
            Command_OknoWyboruSciezki = new Command_OknoWyboruSciezki(navigationStore);
        }

        public Glowny_widok_model()
        {
        }
    }
}
