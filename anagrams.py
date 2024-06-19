import itertools

def create(s):
    res_set = set()
    for permutation in itertools.permutations(s):
        string = ""
        for c in permutation: string+=c
        res_set.add(string)
    return sorted([s for s in res_set])

if __name__ == "__main__":
    print(create("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create("aaaaa")) # ['aaaaa']
    print(create("abab")) # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    print(len(create("aybabtu"))) # 1260