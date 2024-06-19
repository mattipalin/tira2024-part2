import math
def count(x, coins):
    NCIO = {c:1 for c in coins}
    NOS  = {c:1 for c in coins}
    for s in range(1,x+1):
        if s in coins: continue
        mincoin_prev = min([NCIO[s-c] for c in coins if s-c>0])
        NOS[s] = sum([NOS[s-c] for c in coins if s-c>0 and NCIO[s-c]==mincoin_prev])
        NCIO[s] = mincoin_prev + 1
    return NOS[x]
        




if __name__ == "__main__":
    print(count(5, [1])) # 1
    print(count(5, [1, 2, 3, 4])) # 4
    print(count(13, [1, 2, 5])) # 12
    print(count(42, [1, 5, 6, 17])) # 30