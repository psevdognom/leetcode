#https://leetcode.com/problems/median-of-two-sorted-arrays/
#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#The overall run time complexity should be O(log (m+n)).

from typing import List

class Solution:

    def _findMedianOfArray(self, array: List[int]) -> float:
        middle = float(len(array))/2
        if len(array) % 2 == 0:
            return (array[int(middle-0.5)] + array[int(middle+0.5)]) / 2
        else:
            return array[int(middle)]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return (self._findMedianOfArray(nums1) + self._findMedianOfArray(nums2)) / 2