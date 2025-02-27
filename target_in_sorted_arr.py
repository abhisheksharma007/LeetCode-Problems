
def target_in_sorted_arr(nums, target):
    res = -1
    
    left = 0
    right = len(nums)-1
    mid = (left+right)//2
    
    while left < right:
        mid = (left+right)//2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    l = 0
    r = len(nums)-1
    start = left
    
    if target >= nums[start] and target <= nums[r]:
        l = start
    else:
        r = start
    
    while l < r:
        m = (l+r)//2
        if nums[m] < target:
            l = m+1
        else:
            r = m

    if nums[l] == target:
        res = l

    return res


def target_in_sorted_arr(nums, target):
    l = 0
    r = len(nums)-1
    
    while (l <= r):
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[l]:
            if target >= nums[l] and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if target > nums[mid] and target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
    return -1

# nums = [4,5,6,7,0,1,2]
# target = 0

nums = [4,5,6,7,0,1,2]
target = 0

# nums = [1,3]
# target = 3

print(target_in_sorted_arr(nums, target))