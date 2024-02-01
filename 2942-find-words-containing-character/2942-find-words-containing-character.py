class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        l1 = []
        
        
        for ind, word in enumerate(words):
            
            if word.find(x) >-1:
                l1.append(ind)
                
                
        return l1