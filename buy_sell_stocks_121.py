from math import ceil

prices = [7,6,4,3,1]

# prices = [7,1,5,3,6,4]

prices = [7,2,5,3,1,6,4]

# prices = [2,1,4]

def max_profit(prices):
    l, r = 0, 1
    res = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            curr_res = prices[r] - prices[l]
            res = max(res, curr_res)
        else:
            l = r
        r += 1

    return res

print(max_profit(prices))