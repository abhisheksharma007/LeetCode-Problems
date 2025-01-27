def k_most_freq_elememt(nums, k):
    if k < 1 or k > len(nums):
        return []
    if len(nums) == len(set(nums)):
        return nums[:k]
    i = 0
    most_freq = {}
    res_dict = {}
    res = []
    while i < len(nums):
        if nums[i] not in most_freq:
            most_freq[nums[i]] = 1
        else:
            most_freq[nums[i]] += 1
        i+=1

    for key, v in most_freq.items():
        if v not in res_dict:
            res_dict[v] = [key]
        else:
            res_dict[v].append(key)

    for key, v in sorted(res_dict.items(), reverse=True):
        res.extend(v)
        if res and len(res) >= k:
            break
    return res[:k]

from collections import Counter

def k_most_freq_elememt(nums, k):
    nums = Counter(nums)
    nums = dict(sorted(nums.items(), key=lambda item: item[1], reverse=True))
    return list(nums.keys())[:k]


import heapq
def k_most_freq_elememt(nums, k):
    if k == len(nums):
            return nums
    counter = Counter(nums)
    max_heap = []
    heapq.heapify(max_heap)
    for number, frequency in counter.items():
        heapq.heappush(max_heap,(-frequency,number))
    answer = []
    while k:
        answer.append(heapq.heappop(max_heap)[1])
        k -= 1
    return answer

nums = [5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3]
k = 3

curr = k_most_freq_elememt(nums, k)
expected = [3,7,10]
print("curr :", curr)
print("expected :", expected)