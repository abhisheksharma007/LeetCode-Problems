def product_except_self(nums):
    res = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        res[i] *= prefix
        prefix *= nums[i]
    suffix = 1
    for j in range(len(nums)-1, -1, -1):
        res[j] *= suffix
        suffix *= nums[j]
    return res

nums = [10,2,3,4]
print("_______________",product_except_self(nums))