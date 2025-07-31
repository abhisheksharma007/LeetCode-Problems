# contraint O(1) space complexity

nums = [1,3,4,2,2]
# nums = [3,1,3,4,2]
# nums = [3,3,3,3,3]


def find_duplicate(nums):
    s, f = 0, 0
    while True:
        s = nums[s]
        f = nums[nums[f]]
        if s == f:
            break

    s2 = 0
    while True:
        s = nums[s]
        s2 = nums[s2]
        if s == s2:
            return s

print(find_duplicate(nums))

