def count(n):
    if n == 1: return 0
    if n%2 == 0: res = n
    else: res= int((n+1)/2)*int((n-1)/2)
    return res


if __name__ == "__main__":
    #print(count(1)) # 1
    print(count(572589547)) # 81964697333416302