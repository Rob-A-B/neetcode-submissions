class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        dici={')':'(' ,']':'[', '}':'{'}
        for a in s:
            if a in dici.values():
                stack.append(a)
                continue
            elif a in dici:
                if not stack or stack[-1]!=dici[a]:
                    return False
                stack.pop()
        return not stack