
def fib_memo(n):
    memo = {}
    memo[0] = 0
    memo[1] = 1
    def fib_recursion(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = fib_recursion(n-1) + fib_recursion(n-2)
            return memo[n]
    
    result = fib_recursion(n)
    return result


def fib_array(n):
    arr = [0] * n
    arr[1] = 1
    arr[0] = 1
    if n == 1 or n == 2:
        return 1
    for i in range(2, n):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[-1]


if __name__ == '__main__':
    n = 8
    result = fib_memo(n)
    print(result)

    res_arr = fib_array(n)
    print(res_arr)






