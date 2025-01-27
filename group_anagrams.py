def groupAnagrams(strs):
    if len(strs) < 2:
        return [strs]
    anagrams = {}
    for i in range(len(strs)):
        key = ''.join(sorted(strs[i]))
        if key not in anagrams:
            anagrams[key] = [strs[i]]
        else:
            anagrams[key].append(strs[i])
    return list(anagrams.values())



strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["a"]
print(groupAnagrams(strs))