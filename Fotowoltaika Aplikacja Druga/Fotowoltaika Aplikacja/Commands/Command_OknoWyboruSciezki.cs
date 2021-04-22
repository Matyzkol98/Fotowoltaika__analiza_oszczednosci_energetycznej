using Fotowoltaika_Aplikacja.Store;
using Fotowoltaika_Aplikacja.ViewModels;

namespace Fotowoltaika_Aplikacja.Commands
{
    public class Command_OknoWyboruSciezki : CommandClass
    {
        private readonly NavigationStore _navigationStore;

        public Command_OknoWyboruSciezki(NavigationStore navigationStore)
        {
            _navigationStore = navigationStore;
        }
        public override void Execute(object parameter)
        {
            _navigationStore.ObecnyWidokModel = new Okno_wyboru_sciezki_model();
        }
    }
}
