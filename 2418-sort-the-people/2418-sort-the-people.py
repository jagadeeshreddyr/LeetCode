class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        s = dict(zip( heights,names))
        
        
        sorted_s = dict(sorted(s.items(),reverse = True ))
        
        sorted_values = list(sorted_s.values())
        
        return sorted_values