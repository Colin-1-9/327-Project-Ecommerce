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
        logging.info(f"[Producer {name} | PID {os.getpid()}, Produced {item}]")
        queue.put(item)
        time.sleep(0.5)

def Consumer(name, queue):
    while True:
        item = queue.get()
        if item is None:
            logging.info(f"[Consumer {name} | PID: {os.getpid()} | Process: Shutting Down]")
            break
        logging.info(f"[Consumer {name} | PID: {os.getpid()}, Consumed {item}]")
        time.sleep(0.3)

def main():
    q = Queue(maxsize=3)
    producers = [Process(target=Producer, args=(f"Producer-{i}", q)) for i in range(3)]
    consumers = [Process(target=Consumer, args=(f"Consumer-{i}", q)) for i in range(3)]
    
    for p in producers: p.start()
    for c in consumers: c.start()
    for p in producers: p.join()
    for c in consumers: c.join()

    def terminating_producers(queue, producers):
        for _ in producers:
            queue.put(None)
        for p in producers:
            p.join()

    def terminating_consumers(queue, consumers):
        for _ in consumers:
            queue.put(None)
        for c in consumers:
            c.join()
    terminating_producers(q, producers)
    terminating_consumers(q, consumers)

    print("Buffer Empty")
    print("All processes have completed.")

main()
