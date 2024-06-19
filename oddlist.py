import itertools

def count(n,x):
    numbers = range(1,n+1)
    res = 0
    for permutation in itertools.permutations(numbers):
        if(valid(permutation,x)):res+=1
    return res

def valid(lst,x):
    if lst[0]!=x: return False
    differences = set()
    for i in range(0, len(lst)-1):
        if lst[i]+lst[i+1] not in differences:
            differences.add(lst[i]+lst[i+1])
        else: return False
    return True

if __name__ == "__main__":
    print(count(1, 1)) # 1
    print(count(4, 2)) # 4
    print(count(8, 5)) # 830