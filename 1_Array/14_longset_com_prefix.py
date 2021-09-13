def longestCommonPrefix(strs) -> str:
    # check if a given substring is common
    def is_common(strs, mid):
        common = strs[0][0:mid]
        n = len(strs)
        for i in range(n):
            current = strs[i][0:mid]
            if common != current:
                return False
        return True

    n = len(strs)
    if n == 1:
        return strs[0]
    max_len = 0
    # find the maximum length of strings
    for i in range(n):
        max_len = max(len(strs[i]), max_len)
    left = 0
    right = len(strs[0])-1
    while left <= right:
        mid = (left + right)//2
        if is_common(strs, mid):
            left = mid + 1
        else:
            right = mid - 1
    return strs[0][0:(left+right)//2]


if __name__ == "__main__":
    strs = ["flower","flower","flower","flower"]
    lcs = longestCommonPrefix(strs)