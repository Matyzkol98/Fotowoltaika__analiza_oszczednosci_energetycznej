using Fotowoltaika_Aplikacja.Store;
using Fotowoltaika_Aplikacja.ViewModels;

namespace Fotowoltaika_Aplikacja.ViewModels
{
    public class Main_Window_View_Model : ViewModelBase
    {
        private readonly NavigationStore _navigationStore;
        public ViewModelBase ObecnyWidokModel => _navigationStore.ObecnyWidokModel;
        public Main_Window_View_Model(NavigationStore navigationStore)
        {
            _navigationStore =  navigationStore;
            _navigationStore.ObecnyWidokModelZmieniony += OnCurrentViewModelChanged;
        }

        private void OnCurrentViewModelChanged()
        {
            OnPropertyChanged(nameof(ObecnyWidokModel));
        }
    }
}
