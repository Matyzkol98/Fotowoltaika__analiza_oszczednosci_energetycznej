using Fotowoltaika_Aplikacja.Commands;
using Fotowoltaika_Aplikacja.Store;
using System.Windows.Input;

namespace Fotowoltaika_Aplikacja.ViewModels
{
    public class Glowny_widok_model : ViewModelBase
    {

        public static int tryb;
        public ICommand Command_OknoWyboruSciezki_dob
        { 
            get;
        }

        public ICommand Command_OknoWyboruSciezki_godz
        {
            get;
        }

        public ICommand Command_OknoWyboruSciezki_mies
        {
            get;
        }


       

        public Glowny_widok_model()
        {
        }



       public Glowny_widok_model(NavigationStore navigationStore)
        {
            Command_OknoWyboruSciezki_godz = new Command_OknoWyboruSciezki(navigationStore);
            Command_OknoWyboruSciezki_dob = new Command_OknoWyboruSciezki(navigationStore);
            Command_OknoWyboruSciezki_mies = new Command_OknoWyboruSciezki(navigationStore);
        }

        

        

    }
}
