# By: Thomas Johnson
from multiprocessing import Process, Queue
import os
import time
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def Producer(name, queue):
    for i in range(3):
        item = f"Item: {i}, Product: {name}"
        logging.info(f"[Producer {name} | PID {os.getpid()}, Produced {item}]")
        queue.put(item)
        time.sleep(0.5)
    queue.put(None) 

def Consumer(name, queue):
    while True:
        item = queue.get()
        if item is None:
            break
        logging.info(f"[Consumer {name} | PID: {os.getpid()}, Consumed {item}]")
        time.sleep(0.3)
    print("Consumer Done.")
            
def main():
    q = Queue(maxsize=3)
    producers = [Process(target=Producer, args=(f"Producer-{i}", q)) for i in range(3)]
    consumers = [Process(target=Consumer, args=(f"Consumer-{i}", q)) for i in range(3)]
    
    for p in producers: p.start()
    for c in consumers: c.start()
    for p in producers: p.join()
    for c in consumers: c.join()

    print("\n Buffer Empty")
    print("All processes have completed.")

main()
