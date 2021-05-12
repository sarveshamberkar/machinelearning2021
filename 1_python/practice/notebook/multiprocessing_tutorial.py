import time
import multiprocessing
import concurrent.futures
from random import randint
import multiprocessing
from time import sleep


def do_something(sec):
    print('Sleeping {sec} sec'.format(sec=sec))
    time.sleep(sec)
    return f'done sleeping for {sec}'


def wait_rand(sec):
    sleep(sec)
    print(f'done sleeping for {sec}')


if __name__ == '__main__':
    start = time.perf_counter()
    # p = []
    # for i in range(10):
    #     p1 = multiprocessing.Process(target=do_something,args=[5])
    #     p1.start()
    #     p.append(p1)
    # for i in p:
    #     i.join()
    #

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     secs = [5, 4, 3, 2, 1]
    #     results = executor.map(do_something, secs)
    #
    #     for result in results:
    #         print(result)
    # finish = time.perf_counter()
    # print(finish - start)

    num_process = 3

    processes = []
    for i in range(num_process):
        p = multiprocessing.Process(target=wait_rand, args=[randint(1, 5)])
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
