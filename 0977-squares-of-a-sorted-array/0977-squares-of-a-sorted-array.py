class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[]
        ans=[]
        for i in nums:
            a.append(abs(i))
        b=sorted(a)
        for val in b:
            a1=val**2
            ans.append(a1)
        return ans