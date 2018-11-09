class Solution:
    def maximalSquare(self, matrix):
		"""
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n) ] for j in range(m)]
        max_len =0 
        for i in range(m):
            for j in range(n):
                if i==0 or j ==0:
                    dp[i][j]=int(matrix[i][j])
                    
                else:
                    if int(matrix[i][j])==1:
                        dp[i][j] = min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))+1
                max_len =max(max_len,dp[i][j])
        print(dp)             
        return max_len*max_len


	