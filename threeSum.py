def three_sum(nums):
    if len(nums) < 3:
        return []

    if len(nums) == 3:
        return [nums] if sum(nums) == 0 else []

    nums.sort()
    res = []
    l = 0
    right = len(nums) - 1
    for i in range(len(nums)-2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i+1
        r = right
        target = -nums[i]
        while l < r:
            if nums[r] + nums[l] < target:
                l += 1
            elif nums[r] + nums[l] > target:
                r -= 1     
            else:
                res.append([nums[l], nums[r], nums[i]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                l += 1
                r -= 1
                
    return res


nums = [-1,0,1,2,-1,-4]
print(nums)
print("exp ",[[-1,-1,2],[-1,0,1]])
print(three_sum(nums))
