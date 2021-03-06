def maxSubArray(nums) -> int:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1]+nums[i])
    return max(dp)

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))    