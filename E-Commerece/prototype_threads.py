# By: Thomas Johnson
from multiprocessing import Process, Queue
import os
import time
import queue
# Messege queues
q = queue.Queue(maxsize=3)

# Sellers inventory
def producer(name, queue):
    for i in range(3):
        item = f"Item: {i}, Product: {name}"
        print(f"[Producer{name} | PID {os.getpid()}, Process {item}]")
        queue.put(item)
        time.sleep(0.5)

#Buyers
def Consumer(name, queue):
    item = queue.get()
    print(f"Consumer{name} | PID: {os.getpid()}, Process {item}")
    time.sleep(0.3)

def main():
    pass
