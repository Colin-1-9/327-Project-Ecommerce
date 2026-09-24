# By: Thomas Johnson
from multiprocessing import Process, Queue
import os
import time
import queue

q = queue.Queue(maxsize=3)

def producer(name, queue):
    for i in range(3):
        item = f"Item: {i}, Product: {name}"
        print(f"[Producer{name} | PID {os.getpid()}, Process {item}]")
        queue.put(item)

def buyer(name, queue):
    pass

def main():
    pass