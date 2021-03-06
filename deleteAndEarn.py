﻿#TimeComplexity:O(N) where N is max element in given List.
#SpaceComplexity: O(N)
#Did this code successfully run on Leetcode : Yes 
#Any problem you faced while coding this : 
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1=[0]*(max(nums)+1)
        for i in nums:
            nums1[i]=nums1[i]+i
        c=0
        dc=0
        temp=0
        for i in range (len(nums1)):
            temp=c
            c=nums1[i]+dc
            dc=max(temp,dc)
        return max(c,dc)
