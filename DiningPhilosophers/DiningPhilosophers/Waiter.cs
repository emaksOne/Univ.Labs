using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net.Configuration;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace DiningPhilosophers
{
    public class Waiter
    {
        static private Waiter instance;

        static public Waiter Instance
        {
            get
            {
                if(instance == null)
                    instance = new Waiter();
                return instance;
            }
        }
        private Semaphore semaphore;
        private List<Fork> forks;

        private void SetForks(List<Fork> diningForks)
        {
            forks = diningForks;
        }

        private void SetSemaphore()
        {
            semaphore = new Semaphore(forks.Count-1,forks.Count-1);
        }

        public void InitWaiter(List<Fork> forks)
        {
            SetForks(forks);
            SetSemaphore();
        }

        public void GiveForks(Fork leftFork, Fork rightFork, int philosopherNum, int thinkingTime, int eatingTime)
        {

            Console.WriteLine("\tPhilosopher {0} is speaking", philosopherNum);
            Thread.Sleep(thinkingTime * 1000);
            if (leftFork.IsChosen || rightFork.IsChosen)
                Console.WriteLine("\tPhilosopher {0} is waiting for free forks", philosopherNum);

            semaphore.WaitOne();

            lock (leftFork)
            {
                leftFork.IsChosen = true;
                //Console.WriteLine("\tPhilosopher {0} took fork {1}", philosopherNum, leftFork.Number);

                {
                    lock (rightFork)
                    {
                        leftFork.IsChosen = true;
                        //Console.WriteLine("\tPhilosopher {0} took fork {1}", philosopherNum, rightFork.Number);
                        Console.WriteLine("Philosopher {0} is eating", philosopherNum);
                        Thread.Sleep(eatingTime * 1000);
                    }
                    rightFork.IsChosen = false;
                    //Console.WriteLine("\tPhilosopher {0} released fork {1}", philosopherNum, rightFork.Number);
                }
            }
            leftFork.IsChosen = false;

            //Console.WriteLine("\tPhilosopher {0} released fork {1}", philosopherNum, leftFork.Number);

            semaphore.Release(1);
        }
    }
}
