class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for char in s:
            s_dict[char] = 1 + s_dict.get(char, 0)

        for char in t:
            t_dict[char] = 1 + t_dict.get(char, 0)
   
        for value in s_dict:
               
            if (s_dict[value] != t_dict.get(value, 0)):
                return False

        return True