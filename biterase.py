def remove_index(s,i):
    # given string s, returns the string with character removed from positions i and i+1
    return s[:i] + s[i+2:]

count_dict = {"01": 1, "10": 1}
def count(s):
    if len(s)%2 == 1: return 0
    if not s: return 0
    if s=="01" or s == "10": return 1
    res = 0
    # Find removable indices
    removable_indices = [value for value in [i if s[i]!=s[i+1] else -1 for i in range(len(s)-1)] if value != -1]
    # Then let's remove some indices!
    for index_removed in removable_indices:
        shortened = remove_index(s,index_removed)
        if shortened not in count_dict:
            count_dict[shortened] = count(shortened)
        res += count_dict[shortened]
    return res

if __name__ == "__main__":
    print(count("1001")) # 2
    print(count("1100")) # 1
    print(count("101100")) # 5
    print(count("11001")) # 0
    print(count("01110100100110")) # 6027