import time

def sulku_oma(n):
    res = 1
    for multiplier in range(n//2 +1,n +1):
        res*= multiplier/(n+1-multiplier)
    return int(res/(n//2 + 1))


def count_sequences(n, d=0, result={}):
    if d < 0 or d > n:
        return 0
    if n == 0:
        return 1
    if (n, d) not in result:
        result[(n, d)] = count_sequences(n - 1, d + 1) + \
                         count_sequences(n - 1, d - 1)
    return result[(n, d)]


min = 320

# Oma
st = time.time()
for k in range(min,min+11):
    print(2*k, sulku_oma(2*k))
et = time.time()
print("Oma: ", et- st)

# Count_sequances
st = time.time()
for k in range(min,min+11):
    print(2*k, count_sequences(2*k))
et = time.time()
print("Count_sequences: ", et- st)