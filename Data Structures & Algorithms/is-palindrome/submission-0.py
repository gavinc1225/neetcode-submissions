class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(char.lower() for char in s if char.isalnum())
        
        left = 0;
        right = len(res)
        right -= 1
        while (left < right):
            if(res[left] != res[right]):
                return False
            left += 1
            right -= 1

        return True