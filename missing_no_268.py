nums = [3,0,1]
out = 2

def missingNumber(nums):
    return sum(range(0, len(nums)+1)) - sum(nums)


print(missingNumber(nums))