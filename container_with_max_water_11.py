
def max_area(height):
    curr_a = max_a = 0
    l = 0
    r = len(height)-1
    while l < r:
        if height[l] < height[r]:
            curr_a = height[l] * (r-l)
            l += 1
        else:
            curr_a = height[r] * (r-l)
            r -=1
        if curr_a > max_a:
            max_a = curr_a
    return max_a
    


height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))
print(49)