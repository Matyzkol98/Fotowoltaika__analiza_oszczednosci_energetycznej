using Fotowoltaika_Aplikacja.Store;
using Fotowoltaika_Aplikacja.ViewModels;

namespace Fotowoltaika_Aplikacja.Commands
{
    public class Command_GlownyWidok : CommandClass
    {
        private readonly NavigationStore _navigationStore;

        public Command_GlownyWidok(NavigationStore navigationStore)
        {
            _navigationStore = navigationStore;
        }
        public override void Execute(object parameter)
        {
            _navigationStore.ObecnyWidokModel = new Glowny_widok_model(_navigationStore);
        }
    }
}
