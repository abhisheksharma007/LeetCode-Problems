# Given two strings s1 and s2, check if both the strings are anagrams of each other.
# Examples: 

# Input : s1 = "listen"
#         s2 = "silent"
# Output : The strings are anagrams.


# Input : s1 = "dad"
#         s2 = "bad"
# Output : The strings aren't anagrams.



# s1 = "listen"
s2 = "silent"
z = list(s2)
q = z
q.append('x')
print(hex(id(z)))
print(hex(id(q)))
print("_____________")
x = 10
print(hex(id(x)))
y = x
print(hex(id(y)))
y += 1
print(hex(id(y)))

s1 = "dad"
s2 = "bad"

# s1 = 'sssdsassa'
# s2 = 'assssassd'



def check_anagram(s1, s2):
    
    res_anagrams = 'The strings are anagrams'
    res_notanagrams = 'The strings aren\'t anagrams'
    
    s1_arr = list(s1)
    s2_arr = list(s2)
    
    if len(s1) != len(s2):
        return res_notanagrams
    
    for i in s1_arr:
        if i not in s2:
            return res_notanagrams
        
        try:
            s2_arr.remove(i)
        except:
            return res_notanagrams
    
    if not s2_arr:
        return res_anagrams
        
    return res_notanagrams



print(check_anagram(s1, s2))



