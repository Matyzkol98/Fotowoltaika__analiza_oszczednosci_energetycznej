using System.Windows.Input;
using Fotowoltaika_Aplikacja.Commands;
using Fotowoltaika_Aplikacja.Store;
using Fotowoltaika_Aplikacja.Classes;
using Fotowoltaika_Aplikacja.Views;
using System.Windows.Controls;
using System;
using System.Windows;
using System.Diagnostics;

namespace Fotowoltaika_Aplikacja.ViewModels
{
    public class Pokaz_wyniki_model : ViewModelBase
    {
                    // część nawigacyjna //

        private NavigationStore navigationStore;

        public ICommand Command_OknoWyboruSciezki
        {
            get;
        }

        public Pokaz_wyniki_model(NavigationStore navigationStore)
        {
            Debug.WriteLine("Teraz obsluguje przycisk Powrotu");
            this.navigationStore = navigationStore;
            Command_OknoWyboruSciezki = new Command_OknoWyboruSciezki(navigationStore);
        }

        // koniec części nawigacyjnej //

        // Obsługa przycisków //
        
        private ICommand _clickCommand;
        public int x;

        public ICommand Rysujwykres
        {
            get
            {
                return _clickCommand ?? (_clickCommand = new CommandHandler(() => MyAction(x=1), () => CanExecute));
            }
            set
            {
                x = 1;
            }
        }
        
        public ICommand Zaladujplik
        {
            get
            {
                return _clickCommand ?? (_clickCommand = new CommandHandler(() => MyAction(x=0), () => CanExecute));
            }
            set
            {
                x = 0;
            }
        }
        public bool CanExecute
        {
            get
            {
                return true || false;
            }
        }

        
        public void MyAction(int x)
        {
            if (x == 1)
            {
                Debug.WriteLine("Teraz obsluguje przycisk Rysowania");
                Obsluga_Interfejsu.rysowanie_wykresu();
            }
            else if (x == 0)
            {
                Debug.WriteLine("Teraz obsluguje przycisk BazeDanych");
                //Obsluga_Interfejsu.otworz_open_dialog();
                
                Obsluga_Interfejsu.zaladuj_z_bazy_do_datagrid();
            }    
        }

       

       
    
          

        public class CommandHandler : ICommand
        {
            private Action _action;
            private Func<bool> _canExecute;
            public CommandHandler(Action action, Func<bool> canExecute)
            {
                _action = action;
                _canExecute = canExecute;
            }

            public event EventHandler CanExecuteChanged
            {
                add { CommandManager.RequerySuggested += value; }
                remove { CommandManager.RequerySuggested -= value; }
            }

            public bool CanExecute(object parameter)
            {
                return _canExecute.Invoke();
            }

            public void Execute(object parameter)
            {
                _action();
            }
        }
        
        // Koniec obsługi przycisków //

    }
}
