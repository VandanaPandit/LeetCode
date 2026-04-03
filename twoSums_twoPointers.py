def two_sums(nums, target):
    nums_with_idx = [(num,i) for i, num in enumerate(nums)]
    nums_with_idx.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums_with_idx[left][0] + nums_with_idx[right][0]
        if current_sum == target:
            return[nums_with_idx[left][1],nums_with_idx[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return[]

nums = [2, 7, 11, 15]
target = 9

print(two_sums(nums, target))