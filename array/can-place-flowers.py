class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] !=1 and flowerbed[i]!=1:
                flowerbed[i-1] = 1
                n = n-1
            elif flowerbed[i] !=1 and flowerbed[i+1]!=1:
                flowerbed[i+1] = 1
                n = n-1
        
            if n ==0:
                return True
            else:
                return False