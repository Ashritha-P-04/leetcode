class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            leftSum=sum(nums[:i+1])
            Rightsum=sum(nums[i:])
            if leftSum==Rightsum:
                return i
        return -1
        