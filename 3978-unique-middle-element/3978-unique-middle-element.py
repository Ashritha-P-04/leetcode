class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid=len(nums)//2
        element=nums[mid]
        count=0
        for i in nums:
            if i==element:
                count+=1
        if count==1:
            return True
        else:
            return False
        