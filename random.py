import math
import time
from time import sleep
print("Random.py v.1.0.1")
f = []

def current_milli_time():
    return round(time.time() * 1000)
global seed
def LCG(a):
    global seed
    seed = a
def r(a):
    b = 2 ** 127
    c = 49094842449
    global seed
    seed = (a*seed + c) % b
    return seed
def rand():
    LCG(current_milli_time())
    f.append(r(current_milli_time()))
    for i in range(10):
        LCG(f[-1])
        f.append(r(current_milli_time()))
        sleep(0.0000317)
def penguinrandom():
    rand()
    t = 0
    s = f[current_milli_time() % 10]
    t ^= t<< 36
    t ^= t<<16
    t ^= s^(s<< 35)
    if (current_milli_time()^23)%2==0:
      t ^=s>>10^t
    else:
      t^=s<<10^t
    return (t * 5239002234 // 10)%current_milli_time()
g = []
temp = 0
x = current_milli_time()
print(x)
for i in range(100):
    print(penguinrandom())
print(current_milli_time()-x)
#Highest is 887 ms, lowest is 239 ms, seems to not exceed 1s most of the time.