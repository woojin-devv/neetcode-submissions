class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            elif ch == ")" or ch == "]" or ch == "}":
                if len(stack) == 0:
                    return False

                temp = stack.pop()
                result = temp + ch

                if result != "()" and result != "{}" and result != "[]":
                    return False
                    
        return len(stack) == 0
        