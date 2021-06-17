using System.Windows.Input;
using Fotowoltaika_Aplikacja.Commands;
using Fotowoltaika_Aplikacja.Store;
using System.Diagnostics;
using Fotowoltaika_Aplikacja.Classes;
using System;

namespace Fotowoltaika_Aplikacja.ViewModels
{
    public class Okno_wyboru_sciezki_model:ViewModelBase
    {

        private ICommand _clickCommand;

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
            get
            {
                return _clickCommand ?? (_clickCommand = new CommandHandler(() => MyAction(), () => CanExecute));
            }
        }
        /// <summary>
        /// /Tu ważny fragment
        /// </summary>
        

        public bool CanExecute
        {
            get
            {
                return true || false;
            }
        }

        public void MyAction()
        {
            Obsluga_Interfejsu.otworz_open_dialog();
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


            /*public string _textbox1;
            public string _textbox3;
            public string TxtBox1
            {
                get { return _textbox1; }
                set
                {
                    if (value != _textbox1)
                    {
                        _textbox1 = value;
                        OnPropertyChanged("TxtBox1");
                    }
                }
            }
            public string TxtBox3
            {
                get { return _textbox3; }
                set
                {
                    if (value != _textbox3)
                    {
                        _textbox3 = value;
                        OnPropertyChanged("TxtBox3");
                    }
                }
            }
            */

        }
    }
}
