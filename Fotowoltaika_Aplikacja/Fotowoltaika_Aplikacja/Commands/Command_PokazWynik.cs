using Fotowoltaika_Aplikacja.Store;
using Fotowoltaika_Aplikacja.ViewModels;

namespace Fotowoltaika_Aplikacja.Commands
{
    public class Command_PokazWynik : CommandClass
    {
        private readonly NavigationStore _navigationStore;

        public Command_PokazWynik(NavigationStore navigationStore)
        {
            _navigationStore = navigationStore;
        }
        public override void Execute(object parameter)
        {
            _navigationStore.ObecnyWidokModel = new Pokaz_wyniki_model(_navigationStore);
        }
    }
}
