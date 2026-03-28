# intentionally_broken_script.py
# This file intentionally contains MANY types of errors for AI debugging tests

import os
import sys
import json
import math
import random
import time
import threading
import numpy as np
import pandas as pd
import torch
import sklearn
import matplotlib.pyplot as plt
import requests
import collections
import itertools
import heapq
import functools
import statistics
import datetime
import logging
import hashlib
import socket
import sqlite3
import asyncio
import re
import base64
import pickle
import subprocess
import multiprocessing
import uuid

# many unused imports above


############################################
# Global variables
############################################

MAX_SIZE = 10
numbers = [1,2,3,4,5]
config = {"retry": 3, "timeout": 5}


############################################
# Function with syntax error
############################################

def add_numbers(a, b)
    return a + b


############################################
# Runtime division by zero
############################################

def divide(a, b):
    return a / b


############################################
# Name error
############################################

def greet(name):
    print("Hello " + username)


############################################
# Type error
############################################

def multiply(a, b):
    return a * "string"


############################################
# Index out of bounds
############################################

def get_item(lst, index):
    return lst[index]


############################################
# Infinite loop
############################################

def infinite_loop():
    while True:
        print("Running forever")


############################################
# Bad recursion
############################################

def recursive_function(n):
    return recursive_function(n+1)


############################################
# File read error
############################################

def read_file():
    f = open("non_existing_file.txt", "r")
    content = f.read()
    f.close()
    return content


############################################
# Memory misuse
############################################

def allocate_large_memory():
    arr = [0] * (10**9)
    return arr


############################################
# Logical bug
############################################

def average(lst):
    total = 0
    for i in range(len(lst)+1):
        total += lst[i]
    return total / len(lst)


############################################
# Class misuse
############################################

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


############################################
# Incorrect class usage
############################################

def create_person():
    p = Person("Alice")
    p.display()


############################################
# Thread bug
############################################

def thread_task():
    for i in range(5)
        print(i)


############################################
# Network error
############################################

def fetch_data():
    response = requests.get("http://localhost:9999/api")
    return response.json()


############################################
# JSON bug
############################################

def parse_json():
    data = '{"name": "John", "age": 30'
    return json.loads(data)


############################################
# Sorting bug
############################################

def sort_numbers():
    nums = [5,3,6,2,1]
    nums.sort(reverse="yes")
    return nums


############################################
# Wrong numpy usage
############################################

def numpy_error():
    arr = np.array([1,2,3])
    return arr[10]


############################################
# Async misuse
############################################

async def async_task():
    return "done"

def run_async():
    return async_task()


############################################
# Pandas bug
############################################

def pandas_bug():
    df = pd.DataFrame({"a":[1,2], "b":[3,4]})
    return df["c"]


############################################
# Dictionary key error
############################################

def dict_error():
    data = {"x":1,"y":2}
    return data["z"]


############################################
# Math error
############################################

def sqrt_error():
    return math.sqrt(-1)


############################################
# Wrong unpacking
############################################

def unpack_error():
    a, b, c = [1,2]
    return a+b+c


############################################
# Broken generator
############################################

def broken_generator():
    yield 1
    raise StopIteration
    yield 2


############################################
# Main function
############################################

def main():

    print(add_numbers(5,3))

    print(divide(5,0))

    greet("Soham")

    print(multiply(5,10))

    print(get_item(numbers, 100))

    avg = average(numbers)
    print("Average:", avg)

    create_person()

    thread = threading.Thread(target=thread_task)
    thread.start()

    print(fetch_data())

    print(parse_json())

    print(sort_numbers())

    print(numpy_error())

    print(run_async())

    print(pandas_bug())

    print(dict_error())

    print(sqrt_error())

    print(unpack_error())

    for x in broken_generator():
        print(x)

    allocate_large_memory()

    infinite_loop()


############################################
# Script execution
############################################

if __name__ == "__main__":
    main()
