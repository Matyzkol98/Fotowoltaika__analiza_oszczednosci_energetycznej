﻿#pragma checksum "..\..\..\..\Views\GlownyWidok.xaml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "979357D58C2F460DE28DCE11B1A7594EBED308BF"
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using Fotowoltaika_Aplikacja.Views;
using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Controls.Ribbon;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Markup;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Effects;
using System.Windows.Media.Imaging;
using System.Windows.Media.Media3D;
using System.Windows.Media.TextFormatting;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Shell;


namespace Fotowoltaika_Aplikacja.Views {
    
    
    /// <summary>
    /// MainView
    /// </summary>
    public partial class MainView : System.Windows.Controls.UserControl, System.Windows.Markup.IComponentConnector {
        
        
        #line 10 "..\..\..\..\Views\GlownyWidok.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button Rap_dobowy;
        
        #line default
        #line hidden
        
        
        #line 11 "..\..\..\..\Views\GlownyWidok.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button Rap_miesieczny;
        
        #line default
        #line hidden
        
        
        #line 12 "..\..\..\..\Views\GlownyWidok.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button Rap_roczny;
        
        #line default
        #line hidden
        
        private bool _contentLoaded;
        
        /// <summary>
        /// InitializeComponent
        /// </summary>
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "5.0.4.0")]
        public void InitializeComponent() {
            if (_contentLoaded) {
                return;
            }
            _contentLoaded = true;
            System.Uri resourceLocater = new System.Uri("/Fotowoltaika Aplikacja;V1.0.0.0;component/views/glownywidok.xaml", System.UriKind.Relative);
            
            #line 1 "..\..\..\..\Views\GlownyWidok.xaml"
            System.Windows.Application.LoadComponent(this, resourceLocater);
            
            #line default
            #line hidden
        }
        
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "5.0.4.0")]
        [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Never)]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Design", "CA1033:InterfaceMethodsShouldBeCallableByChildTypes")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Maintainability", "CA1502:AvoidExcessiveComplexity")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1800:DoNotCastUnnecessarily")]
        void System.Windows.Markup.IComponentConnector.Connect(int connectionId, object target) {
            switch (connectionId)
            {
            case 1:
            this.Rap_dobowy = ((System.Windows.Controls.Button)(target));
            
            #line 10 "..\..\..\..\Views\GlownyWidok.xaml"
            this.Rap_dobowy.Click += new System.Windows.RoutedEventHandler(this.przycisk_raport_dobowy);
            
            #line default
            #line hidden
            return;
            case 2:
            this.Rap_miesieczny = ((System.Windows.Controls.Button)(target));
            
            #line 11 "..\..\..\..\Views\GlownyWidok.xaml"
            this.Rap_miesieczny.Click += new System.Windows.RoutedEventHandler(this.przycisk_raport_miesieczny);
            
            #line default
            #line hidden
            return;
            case 3:
            this.Rap_roczny = ((System.Windows.Controls.Button)(target));
            
            #line 12 "..\..\..\..\Views\GlownyWidok.xaml"
            this.Rap_roczny.Click += new System.Windows.RoutedEventHandler(this.przycisk_raport_roczny);
            
            #line default
            #line hidden
            return;
            }
            this._contentLoaded = true;
        }
    }
}

