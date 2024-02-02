class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',                                      'v','w','x','y', 'z']
        l2 = list(sentence)
        
        for let in l1:
            
            if let not in l2:
                return False
            
        return True