using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace DiningPhilosophers
{
    public class Philosopher
    {
        public int Number { get; set; }

        public Philosopher(int number)
        {
            Number = number;
        }
        private int SpeakingTime
        {
            get { return GetRandomTime(); }
        }

        private int EatingTime
        {
            get { return GetRandomTime(); }
        }

        private int GetRandomTime()
        {
            Random rand = new Random();
            return rand.Next(2,6);
        }
        public void Eat(Fork leftFork, Fork rightFork)
        {
            while (true)
            {
                Waiter.Instance.GiveForks(leftFork, rightFork, Number, SpeakingTime, EatingTime);
            }
        }
    }
}
