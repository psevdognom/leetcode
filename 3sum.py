#https://leetcode.com/problems/3sum/
# When discussing "three sums" in the context of Python programming, it often refers to a problem that involves finding sets of three numbers within an array that sum up to a specific target number. This problem is commonly known as the "3Sum" problem. It's a classic algorithmic challenge used in coding interviews and algorithm practice. The goal is to identify all unique triplets in the array which gives the sum of zero (or another target value).
#
# Here's a general approach to solve the 3Sum problem:
#
# Sort the array: This makes it easier to avoid duplicates and use two pointers to scan through the array efficiently.
#
# Iterate through the array: Use a loop to consider each element a as the first element of the triplet. For each element, you'll try to find two other elements b and c such that a + b + c = 0.
#
# Two pointers approach: For each element a, set two pointers, one at the element immediately after a and another at the end of the array. If the sum of a, b, and c is too large, move the end pointer to the left. If the sum is too small, move the start pointer to the right. If the sum is just right, record the triplet and move both pointers, skipping over any duplicate values to avoid repeating triplets.
#
# Avoiding duplicates: Since the problem asks for unique triplets, you'll need to skip over any duplicate values for a, as well as within the two-pointer scan to avoid repeating the same triplets.
#
# Return the list of triplets: Once you've gone through all elements and their two-pointer scans, return the list of found triplets.
#
# Now, let's implement a Python function to solve the 3Sum problem, assuming the target sum is zero:
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        result = []
        for i in range(len(nums) - 2):  # Step 2: Iterate through the array
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for a
                continue
            left, right = i + 1, len(nums) - 1  # Two pointers
            while left < right:  # Step 3: Two pointers approach
                total = nums[i] + nums[left] + nums[right]
                if total < 0:  # Sum too small, move left pointer
                    left += 1
                elif total > 0:  # Sum too large, move right pointer
                    right -= 1
                else:  # Sum just right, add to result and skip duplicates
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return closest_sum