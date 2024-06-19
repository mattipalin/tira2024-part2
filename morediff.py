import itertools
def cre_bruteforce(n):
    res = []
    numbers = range(1,n+1)
    for permutation in itertools.permutations(numbers):
        if(valid(permutation)):
            #res = [permutation.index(i,0,n) for i in numbers]
            res = [i for i in permutation]
            break
    if res: return res
    else: return None

def valid(lst):
    # Difference of adjacent cannot be 1
    for i in range(len(lst)-1):
        if abs(lst[i]-lst[i+1])==1: return False
    return True

def create(n):
    # First, generate arrays of the even and odd entries
    print("n=", n)
    odd_entries = []
    even_entries= []
    for j in range(1,n+1):
        if j%2==1: odd_entries.append(j)
        else: even_entries.append(j)
    print(odd_entries)
    print(even_entries)

if __name__ == "__main__":
    #print(cre_bruteforce(1)) # [1]
    #print(cre_bruteforce(2)) # None
    #print(cre_bruteforce(3)) # None
    #print(cre_bruteforce(4)) # [2, 4, 1, 3]
    #print(cre_bruteforce(5)) # [1, 3, 5, 2, 4]
    #print(cre_bruteforce(6)) # [1, 3, 5, 2, 4, 6]
    #print(cre_bruteforce(7)) # [1, 3, 5, 2, 6, 4, 7]
    #print(cre_bruteforce(8)) # [1, 3, 5, 2, 6, 8, 4, 7]
    #print(cre_bruteforce(9)) # [1, 3, 5, 2, 4, 7, 9, 6, 8]
    #print(cre_bruteforce(10))# [1, 3, 5, 2, 4, 6, 8, 10, 7, 9]
    #print(cre_bruteforce(11))# []
    #print(cre_bruteforce(12))# []
    #print(cre_bruteforce(13))# []
    #print(cre_bruteforce(14))# []
    print(create(2))
    print(create(3))
    print(create(4))
    print(create(17))