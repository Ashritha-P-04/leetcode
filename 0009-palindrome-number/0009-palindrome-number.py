class Solution:
    def isPalindrome(self, x: int) -> bool:
        orginal=x
        r=0
        while(x>0):
            ld=x%10
            r=r*10+ld
            x//=10
        if(r==orginal):
            return True
        else:
            return False



        