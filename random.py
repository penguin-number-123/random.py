import math
import time
from time import sleep
print("Random.py 1")
f = []

def current_milli_time():
    return round(time.time() * 1000)
global seed
def LCG(a):
    global seed
    seed = a
def r():
    a = 39081209809
    b = 2 ** 31
    c = 49094842449
    global seed
    seed = (a*seed + c) % b
    return seed
def rand():
    for i in range(10):
        LCG(current_milli_time())
        f.append(r())
        sleep(0.00005)
def penguinrandom():
    rand()
    t = 0
    s = f[current_milli_time() % 10]
    t ^= t<< 36
    t ^= t<<16
    t ^= s^(s<< 35)
    return t * current_milli_time()
g = []
for i in range(10):            
    print(penguinrandom())
    g.append(penguinrandom())


