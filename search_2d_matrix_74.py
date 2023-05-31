matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 13

def find_target(matrix, target):
    if not matrix:
        return False
    
    l = 0
    r = len(matrix)-1
    
    while l <= r:
        mid = (l+r)//2
        if target in matrix[mid]:
            return True
        elif target > matrix[mid][-1]:
            l = mid+1
        else:
            r = mid-1
      
    return False

print(find_target(matrix, target))