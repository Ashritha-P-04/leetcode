class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for val in nums:
            if val%2==0:
                even.append(val)
            else:
                odd.append(val)
        even.extend(odd)
        return even

        