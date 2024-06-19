import itertools

def create(t):
    res = []
    for l in range(len(t)+1):
        for combination in itertools.combinations(t,l):
            res.append(sum(combination))
    return sorted(res)    

if __name__ == "__main__":
    print(create([1, 2, 3])) # [0, 1, 2, 3, 3, 4, 5, 6]
    print(create([42, 1337])) # [0, 42, 1337, 1379]
    print(create([1, 1, 1])) # [0, 1, 1, 1, 2, 2, 2, 3]
    print(create([5])) # [0, 5]