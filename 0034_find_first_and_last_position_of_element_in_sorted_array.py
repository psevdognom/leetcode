class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                output = [start, ]
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                end = i
                output.append(end)
                break
        return output

