class Solution:
    def isValid(self, s: str) -> bool:
        aux=list(s)
        stack=[]
        dici={')':'(' ,']':'[', '}':'{'}
        print(f' a stack no comeco eh {stack}')
        for a in aux:
            print(f' o elemento  atual eh {a}')
            if a in dici.values():
                stack.append(a)
                continue
            if a in dici and not stack:
                return False
            if a  in dici and stack and stack[-1]==dici[a]:
                stack.pop()
            else:
                return False
            
        if len(stack)!=0:
            return False
        else:
            return True