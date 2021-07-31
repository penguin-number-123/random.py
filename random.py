import math
print("Random.py 0.0.1 a")
amount = int(input("How many random numbers do you want?"))
def lcg(a,b,c):
    seed = 2**32
    for i in range(100):
        seed = (a*seed + c) % b
    return seed
