def count(t):
    dictionary = {}
    for i in range(len(t)):
        dictionary[i] = 1
        for j in range(i):
            if t[j]<t[i]:
                dictionary[i]+=dictionary[j]
    return sum([dictionary[i] for i in range(len(t))])

if __name__ == "__main__":
    print(count([1, 1, 2, 2, 3, 3])) # 26
    print(count([1, 1, 1, 1])) # 4
    print(count([5, 4, 3, 2, 1])) # 5
    print(count([4, 1, 5, 6, 3, 4, 1, 8])) # 37