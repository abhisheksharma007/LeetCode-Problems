# def __gen_parenthesis(n, open, close, s, ans):
#     if open == n and close == n:
#         ans.append(s)
#         return
#     if open < n:
#         __gen_parenthesis(n, open+1, close, s+"(", ans)
#     if close < open:
#         __gen_parenthesis(n, open, close+1, s+")", ans)
#     return ans

def genrate_parenthesis(n):
    if n < 1:
        return []
    res = []
    stack = []
    def __gen_parenthesis(open, close, stack):
        if open == n and close == n:
            res.append("".join(stack))
            return
        if open < n:
            stack.append("(")
            __gen_parenthesis(open+1, close, stack)
            stack.pop()
        if close < open:
            stack.append(")")
            __gen_parenthesis(open, close+1, stack)
            stack.pop()

    __gen_parenthesis(0, 0, stack)
    return res

n = 3
print(genrate_parenthesis(n))
expected = ["((()))","(()())","(())()","()(())","()()()"]
print("expected {}".format(expected))