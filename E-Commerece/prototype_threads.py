# By: Thomas Johnson
from multiprocessing import Process, Queue
import os
import time
import random
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def Producer(name, queue):
    for i in range(3):
        item = f"Item: {i}, Product: {name}"
        logging.info(f"[Producer {name} | PID {os.getpid()}, Process {item}]")
        queue.put(item)
        time.sleep(0.5)

def Consumer(name, queue):
    item = queue.get()
    logging.info(f"[Consumer {name} | PID: {os.getpid()}, Process {item}]")
    time.sleep(0.3)

q = Queue(maxsize=3)
processes = [Process(target=Producer, args=(f"Producer-{i}", q)) for i in range(3)]
processes += [Process(target=Consumer, args=(f"Consumer-{i}", q)) for i in range(3)]

def main():
    for p in processes:
        p.start()
    for p in processes:
        p.join()

main()
