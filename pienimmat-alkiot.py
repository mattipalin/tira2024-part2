import random
import heapq
import time


def method1():
    # Create list
    list = []
    for k in range(10**6):
        list.append(random.randrange(10**9))

    # Sort the list
    list.sort()
    return sum(list[0:10**5-1])

def method2():
    # Create list
    list = []
    for k in range(10**6):
        heapq.heappush(list, random.randrange(10**9))
    # Then calculate the sum of the smallest 10^5 items
    sum = 0
    for k in range(10**5): sum+= heapq.heappop(list)
    return sum


st = time.time()
print(method1())
et = time.time()
print("Method1: ", et- st)

st = time.time()
print(method2())
et = time.time()
print("Method2: ", et- st)