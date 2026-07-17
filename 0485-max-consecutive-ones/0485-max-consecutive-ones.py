class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maximum=0
        for val in nums:
            if val==1:
                count+=1
                if count>maximum:
                    maximum=count
            else:
                count=0
        return maximum
        