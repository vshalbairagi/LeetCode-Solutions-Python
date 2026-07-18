class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.x=x
       
        if x<0:
            sign=-1
        else:
            sign=1
            
        x=abs(x)
        rev=0
        while x>0:
            rev=rev*10+x%10
            x=x//10
        
        if -2147483648 >= rev or rev >= 2147483647:
            return 0
        else:    
            return sign*rev
