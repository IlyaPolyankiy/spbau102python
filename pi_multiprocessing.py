import random
import multiprocessing
import time

def countportion(n):
    x = random.random()  
    y = random.random()
    if 1>x*x+y*y:  
        return(4/n)
    return 0

def CountPI(n):
    PI = 0
    for _ in range(n):
        PI += countportion(n)
    return PI

def MultPI(pool):
    pi = 0
    for res in pool.map(CountPI, [n]*cpus):
        pi += res
    pi = pi / cpus
    return pi
        

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    n = 5000000
    cpus = multiprocessing.cpu_count()
    print(f"\nYou have {cpus} threads")
    t1 = time.time()
    PI = MultPI(pool)
    print("1) Result: ", PI)
    print("Time spent with multiprocessing:", time.time() - t1)

    t2 = time.time()
    pi = CountPI(n*cpus)
    print("2) Result multiprocessing:", pi)
    print("Time spent without multiprocessing:", time.time() - t2)
    print("\n")

''''
Мой результат - почти в 6 раз быстрее при такой же точности вычисления:

You have 12 threads
1) Result:  3.141378933415426
Time spent with multiprocessing: 1.857706069946289
2) Result multiprocessing: 3.141552335813683
Time spent without multiprocessing: 10.513164281845093
'''

