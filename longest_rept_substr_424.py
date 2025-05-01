def longest_rep_char(s, k):
    freq_map = {}
    max_freq = 0
    left = 0
    res = 0

    for right in range(len(s)):
        # Update the frequency map for the current character
        freq_map[s[right]] = freq_map.get(s[right], 0) + 1
        max_freq = max(max_freq, freq_map[s[right]])

        # Check if the current window is valid
        while (right - left + 1) - max_freq > k:
            freq_map[s[left]] -= 1
            left += 1

        # Update the result with the size of the valid window
        res = max(res, right - left + 1)

    return res



def longest_rep_char(s, k):
    curr_res = 0
    res = 0
    for i in range(len(s)):
        curr_res = 1
        j, n = i+1, k
        temp_str = s[i]
        while j < len(s):
            if s[j] == temp_str:
                curr_res += 1
            else:
                if n == 0:
                    break
                curr_res += 1
                n -= 1
            j += 1
        if curr_res > res:
            res = curr_res
        
    return res

s = "ABAB"
k = 2
print(longest_rep_char(s, k))