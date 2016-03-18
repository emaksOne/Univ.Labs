using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace DiningPhilosophers
{
    class Program
    {

        static void Main(string[] args)
        {
            DiningProcess proc = new DiningProcess(8);
            Thread thread = new Thread(() =>
            {
                proc.Start();
            });
            thread.Start();

            Console.WriteLine("Press ESC to Stop process");
            ConsoleKeyInfo key = Console.ReadKey();
            if (key.Key.Equals(ConsoleKey.Escape))
            {
                proc.Stop();
                Console.WriteLine("Stop Process");
            }

            Console.ReadLine();
        }
    }
}
