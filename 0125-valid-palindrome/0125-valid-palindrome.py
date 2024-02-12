class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_word=""
        
        for c in s:
            if c.isalnum():
                new_word+=c.lower()
                
        return new_word==new_word[::-1]
        