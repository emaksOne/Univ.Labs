using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DiningPhilosophers
{
    public class Fork
    {
        public int Number { get; set; }
        public bool IsChosen { get; set; }
        public Fork(int number)
        {
            Number = number;
        }
    }
}
