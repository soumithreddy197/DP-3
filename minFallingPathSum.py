﻿#TimeComplexity:O(MN) where M and N are sizes of matrix
#SpaceComplexity: Constant space as we didn't use any extra space.
#Did this code successfully run on Leetcode : Yes 
#Any problem you faced while coding this : No
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        for i in range (1,len(matrix)):
            for j in range (len(matrix[0])):
                if j==0 :
                    matrix[i][j]=matrix[i][j]+min(matrix[i-1][0],matrix[i-1][1])
                elif j==len(matrix[1])-1:
                    matrix[i][j]=matrix[i][j]+min(matrix[i-1][-1],matrix[i-1][-2])
                else:
                    matrix[i][j]=matrix[i][j]+min(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])
        print(matrix)
        return min(matrix[-1])
