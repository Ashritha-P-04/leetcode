class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1=[]
        l2=[]
        ans=[]
        for val in nums:
            if val<0:
                l1.append(val)
            else:
                l2.append(val)
        for i in range(len(l1)):
            ans.append(l2[i])
            ans.append(l1[i])
        return ans

        

        