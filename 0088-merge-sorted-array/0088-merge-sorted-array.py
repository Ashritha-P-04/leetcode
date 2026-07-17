class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1)>m:
            nums1.pop()
        nums1.extend(nums2)
        # for i in range(0,len(nums1):
        #     if nums1[i]==0:
        #         nums1.pop(i)
        nums1.sort()
        # count=0
        # for i in range(len(nums1)):
        #     if nums1[i]==0:
        #         count+=1
        # nums1[:]=nums1[count:]

        # print(nums1)
        # print(nums1)
        # for i in range(len(nums1)):
        #     if nums1[i]==0:
        #         nums1.pop(nums1[i])
        print(nums1)
        