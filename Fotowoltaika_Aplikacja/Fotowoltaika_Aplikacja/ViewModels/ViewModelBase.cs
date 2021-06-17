using System.ComponentModel;
using Fotowoltaika_Aplikacja.Views;

namespace Fotowoltaika_Aplikacja.ViewModels
{
    public class ViewModelBase :  INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler PropertyChanged;

        protected void OnPropertyChanged(string propertyName = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }

    }
}
