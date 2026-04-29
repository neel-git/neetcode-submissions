class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"(":-1, "{":-2, "[":-3, ")":1, "}":2, "]":3}
        stack = []

        for i in range(len(s)):
            if mp.get(s[i]) < 0:
                stack.append(s[i])
            else :
                if len(stack) == 0:
                    return False
                ch = stack[-1]
                stack.pop()
                sum = mp.get(ch) + mp.get(s[i])
                if sum != 0:
                    return False
            
        
        return len(stack) == 0

