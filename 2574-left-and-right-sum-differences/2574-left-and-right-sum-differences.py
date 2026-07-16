class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            leftSum=0
            rightSum=0
            for j in range(len(nums)):
                if i>j:
                    leftSum=leftSum+nums[j]
                if i<j:
                    rightSum=rightSum+nums[j]
            res=abs(leftSum-rightSum)
            l.append(res)
        return l
        