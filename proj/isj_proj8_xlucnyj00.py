#!/usr/bin/env python3

from time import sleep, perf_counter
from threading import Thread
from multiprocessing import Process
import asyncio
 
def work_sleep():
    for i in range(10000): sleep(0)
        
def work_i_square():
    lst = [i*i for i in range(1000000)]
    
async def async_work_i_square():
    lst = [i*i for i in range(1000000)]
        
async def async_work_sleep():
    for i in range(10000): sleep(0)


# Uncomment the following lines to get time report of the performance of each method

def use_multiprocessing():
    # Work sleep
    # start = perf_counter()
    processes = []
    for i in range(100):
        p = Process(target=work_sleep)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    # end = perf_counter()
    # print(f"Multiprocessing work_sleep: {end - start:.2f} s")

    # Work_i_square
    # start = perf_counter()
    processes = []
    for i in range(100):
        p = Process(target=work_i_square)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    # end = perf_counter()
    # print(f"Multiprocessing work_i_square: {end - start:.2f} s")


def use_threading():
    # Work sleep
    # start = perf_counter()
    threads = []
    for i in range(100):
        t = Thread(target=work_sleep)
        t.daemon = True
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    # end = perf_counter()
    # print(f"Threading work_sleep: {end - start:.2f} s")

    # Work_i_square
    # start = perf_counter()
    threads = []
    for i in range(100):
        t = Thread(target=work_i_square)
        t.daemon = True
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    # end = perf_counter()
    # print(f"Threading work_i_square: {end - start:.2f} s")


async def use_asyncio():
    # Work sleep
    # start = perf_counter()
    tasks = [asyncio.create_task(async_work_sleep()) for i in range(100)]
    await asyncio.gather(*tasks)
    # end = perf_counter()
    # print(f"Asyncio work_sleep: {end - start:.2f} s")

    # Work_i_square
    # start = perf_counter()
    tasks = [asyncio.create_task(async_work_i_square()) for i in range(100)]
    await asyncio.gather(*tasks)
    # end = perf_counter()
    # print(f"Asyncio work_i_square: {end - start:.2f} s")


use_multiprocessing()
use_threading()
asyncio.run(use_asyncio())
