using System;
using System.Collections.Generic;
using System.Text;
using Fotowoltaika_Aplikacja.ViewModels;

namespace Fotowoltaika_Aplikacja.Store
{
    public class NavigationStore
    {
        public event Action ObecnyWidokModelZmieniony;

        private ViewModelBase _obecnyWidokModel;
        public ViewModelBase ObecnyWidokModel
        {
            get => _obecnyWidokModel;
            set
            {
                _obecnyWidokModel = value;
                OnCurrentViewModelChanged();
            }
        }

        private void OnCurrentViewModelChanged()
        {
            ObecnyWidokModelZmieniony?.Invoke();
        }
    }
}

