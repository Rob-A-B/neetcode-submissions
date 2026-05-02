class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s): return False

        for c in s:
            if s.count(c)==t.count(c):
                continue
            return False
        return True    