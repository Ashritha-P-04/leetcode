class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l1=[]
        l2=[]
        l3=[]
        for val in nums:
            if val<pivot:
                l1.append(val)
            elif val==pivot:
                l2.append(val)
            else:
                l3.append(val)
        return l1+l2+l3



        