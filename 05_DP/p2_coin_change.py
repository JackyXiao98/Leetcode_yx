"""

322. Coin Change

https://leetcode.com/problems/coin-change/

"""



def coin_memo(coins, amount):
    """
    
    TODO: Consider invalid cases, return -1
    """
    memo = {}
    
    def coin_recursion(n):
        if n < 0:
            return 10**7
        if n == 0:
            return 0
        if n in memo:
            return memo[n]
        memo[n] = min([coin_recursion(n-c) for c in coins]) + 1
        return memo[n]
    
    res = coin_recursion(amount)

    return res, memo


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    res_memo, memo = coin_memo(coins, amount)
    print(res_memo)

    res_arr = 0
    print(res_arr)






