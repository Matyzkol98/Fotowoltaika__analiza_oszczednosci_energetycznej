using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Fotowoltaika_Aplikacja.Classes
{
    public class Dane_Main
    {
        public string Data { get; set; }
        public string Dzien_tygodnia { get; set; }
        public float Pobor_energii { get; set; }
        public float Oddanie { get; set; }
        public float Produkcja { get; set; }
        public float Zuzytkowano_z_fv { get; set; }
        public float Zuzycie_dom {get; set;}

        /*public Dane_Main(string Data, string dzien_tygodnia, float pobor_energii, float oddanie, float produkcja, float zuzytkowano_z_fv, float zuzycie_dom)
        {

        }*/
    }
}
