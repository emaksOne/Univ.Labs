using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Xml.XPath;

namespace DiningPhilosophers
{
    public class DiningProcess
    {
        private int philosophersNum;
        private List<Fork> forks; 
        private List<Philosopher> philosophers;
        private List<Thread> threads;

        public DiningProcess(int philNumb)
        {
            philosophersNum = philNumb;
            forks = new List<Fork>();
            philosophers = new List<Philosopher>();
            threads = new List<Thread>();
            for (int i = 0; i < philosophersNum; i++)
            {
                Philosopher philosopher = new Philosopher(i);
                philosophers.Add(philosopher);
                Fork fork = new Fork(i);
                forks.Add(fork);
            }
            Waiter.Instance.InitWaiter(forks);
        }
        
        public void Start()
        {
            Console.WriteLine("Start process");
            for (int i = 0; i < philosophersNum; i++)
            {
                int ix = i;
                Fork leftFork = forks[ix];
                Fork rightFork = (ix == 0) ? forks[philosophersNum - 1] : forks[ix - 1];
                Thread thread = new Thread(()=>philosophers[ix].Eat(leftFork, rightFork));
                threads.Add(thread);
                thread.Start();
            }
        }

        public void Stop()
        {
            foreach(var thread in threads)
            {
                thread.Abort();
            }
        }
    }
}
