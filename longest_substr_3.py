s = "pwwkewqtexwcaoszepkeewqmtfe"

# s = "abcabcbb"
# s = "aab"

# s ="dvdf"

def longest_substr(s):
    res, curr_res = '', ''
    for i in s:
        while i in curr_res:
            curr_res = curr_res[1:]
        curr_res += i
        if len(curr_res) > len(res):
            res = curr_res

    print(res)
    return len(res)

print(longest_substr(s))