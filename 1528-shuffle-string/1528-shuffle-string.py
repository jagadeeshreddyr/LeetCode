class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        
        s = dict(zip(indices, s))

        sorted_s = dict(sorted(s.items()))

        sorted_values = ''.join(list(sorted_s.values()))

        return sorted_values