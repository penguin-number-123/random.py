import math
import time
from time import sleep
print("Random.py 0.0.1")
amount = int(input("How many random numbers do you want?"))
def current_milli_time():
    return round(time.time() * 1000)
global seed
def LCG(a):
    global seed
    seed = a
def r():
    a = 39081209809
    b = 2 ** 27
    c = 49094842449
    global seed
    seed = (a*seed + c) % b
    return seed
def rand():
    for i in range(amount):
        LCG(current_milli_time())
        print(r())
        sleep(0.001)
rand()