import itertools
result = sorted(set(itertools.permutations("ab")))
res2 = set()
res2.add('a')
res2.add('b')
res2.add('c')
print(result)
print(["".join(x) for x in result])