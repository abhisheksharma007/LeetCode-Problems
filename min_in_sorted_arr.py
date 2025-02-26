def min_in_sorted_arr(nums):        
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (right + left)//2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
    
    
nums = [3,4,5,1,2]
print(min_in_sorted_arr(nums))