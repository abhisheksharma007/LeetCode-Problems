from math import ceil

# piles = [30,11,23,4,20]
# h = 5

# piles = [3,6,7,11]
# h = 8

piles = [312884470]
h = 968709470

def min_bananas_per_hr(piles, h):
    
    if len(piles) == h:
        return max(piles)
    
    l = 0
    r = max(piles)
    res = max(piles)
    
    while l <= r:
        x = 0
        mid = (l+r)//2
        
        if mid == 0:
            return res

        for i in piles:
            x += ceil(i/mid)
        
        if x <= h and mid < res:
            res = mid
        
        if x > h:
            l = mid+1
        else:
            r = mid-1
        
    return res

print(min_bananas_per_hr(piles, h))