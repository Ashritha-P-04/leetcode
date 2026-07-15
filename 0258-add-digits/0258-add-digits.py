class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        while(num>=10):
            sum=0
            while(num>0):
                ld=num%10
                sum+=ld
                num//=10
            num=sum
        return num


        