def count(s):
    # Kun erotellaan osajonot, joissa on samat merkit, osajonoiksi pituudella n_1, n_2, ... niin tulos on
    # (n_1 +1 yli 2) + (n_2 +1 yli 2) + (n_3 +1 yli 2) +  ...
    res = 0
    buffer = s[0]
    n = 1
    for c in s[1:]:     # Ignore first character because it's already in buffer
        if(c != buffer):
            res += int((n+1)*n/2)
            n = 0
            buffer = c
        n+=1
 
    res += int((n+1)*n/2)
    return res
 
if __name__ == "__main__":
    print(count("aaa")) # 6