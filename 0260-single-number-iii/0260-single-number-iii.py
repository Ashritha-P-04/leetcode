class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        for val in nums:
            d[val]=d.get(val,0)+1
        res=[]
        for key,val in d.items():
            if(val==1):
                res.append(key)
        return res