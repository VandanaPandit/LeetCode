def two_sums(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_map:
            return[nums_map[complement], i]
        nums_map[num] = i
    return[]

nums = [2, 7, 11, 15]
target = 9

print(two_sums(nums, target))
