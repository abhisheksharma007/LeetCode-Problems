
def daily_temperatures(temperatures):
    res = [0 for _ in range(len(temperatures))]
    stack = []
    
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            s_ind = stack.pop()
            res[s_ind] = (i - s_ind)
        stack.append(i)
    return res

temperatures = [73,74,75,71,69,72,76,73]
print(daily_temperatures(temperatures))