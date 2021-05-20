using System;
using System.Windows.Input;
using Fotowoltaika_Aplikacja.Commands;
using Fotowoltaika_Aplikacja.Store;
using Fotowoltaika_Aplikacja.Classes;

namespace Fotowoltaika_Aplikacja.Classes
{
    public class Akcja_Reakcja_Na_Przyciski
    {
        private ICommand _clickCommand;

        public ICommand Rysujwykres
        {
            get
            {
                return _clickCommand ?? (_clickCommand = new CommandHandler(() => MyAction1(), () => CanExecute));
            }
        }
        public ICommand Zaladujplik
        {
            get
            {
                return _clickCommand ?? (_clickCommand = new CommandHandler(() => MyAction(), () => CanExecute));
            }
        }

        public bool CanExecute
        {
            get
            {
                return true || false;
            }
        }

        public void MyAction()
        {
            Obsluga_Interfejsu.zaladuj_z_bazy_do_datagrid();
        }
        public void MyAction1()
        {
            Obsluga_Interfejsu.rysowanie_wykresu();
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
    }
}
