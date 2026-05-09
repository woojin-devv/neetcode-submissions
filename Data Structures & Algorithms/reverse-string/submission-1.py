class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        if len(s) % 2 :
            half_len = int(len(s) / 2)
            print(half_len)
        else : 
            half_len = int((len(s) - 1) / 2)

        for i in range(half_len + 1):
            start = i
            end = len(s) - 1 - i
            temp = s[i]
            s[i] = s[end]
            s[end] = temp
        
            




        