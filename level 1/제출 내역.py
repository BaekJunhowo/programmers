def solution(nums):
    from itertools import combinations
    
    lst = list(combinations(nums, len(nums) // 2))
    print(lst)
    return max(map(lambda x: len(set(x)), lst))

def solution(nums):
    from collections import Counter
    d = Counter(nums)
    
    return min(len(d.keys()), len(nums) // 2)