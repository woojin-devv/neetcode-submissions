class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_arr = list(s)
        target = list(t)

        for ch in s_arr:
            if ch in target:
                target.remove(ch)

        if len(target) == 0:
            return True

        return False