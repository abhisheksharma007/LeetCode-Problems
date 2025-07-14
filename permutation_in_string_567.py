from collections import defaultdict, Counter


s1 = "abb"
# s2 = "eidbabooo"

s2 = "eidbbaoo"

s1 = "adc"

s2 = "dcda"

s1 = "hello"
s2 = "ooolleooolleh"


def permutation_in_string(s1, s2):
    res = False
    ln_s1, ln_s2 = len(s1), len(s2)
    if ln_s1 > ln_s2:
        return res
    
    freq_dict = {}
    
    for i in s1:
        freq_dict[i] = freq_dict.get(i, 0) + 1
        
    curr_window = ''
    res_dict = {}
    for i in s2:
        if i in freq_dict:
            res_dict[i] = res_dict.get(i, 0) + 1
            curr_window += i
            if len(curr_window) > ln_s1:
                res_dict[curr_window[0]] -= 1
                curr_window = curr_window[1:]
        else:
            res_dict = {}
            curr_window = ''
        
        if freq_dict == res_dict:
            res = True

    return res


print(permutation_in_string(s1, s2))