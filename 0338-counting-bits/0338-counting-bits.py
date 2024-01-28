class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        st = []
        for i in range(n+1):
            st.append(bin(i).split('b')[1].count('1'))

        return st