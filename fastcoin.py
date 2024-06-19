def count(x):
    n_of_coins = 0
    coins = [5,2,1]
    for coin in coins:
        wholes = x // coin
        rest   = x % coin
        n_of_coins += wholes
        x = rest
    return n_of_coins

if __name__ == "__main__":
    print(count(13)) # 4
    print(count(12345)) # 2469
    print(count(1337**9)) # 2730314408854633746890878156