class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ind = len(digits) -1
        while carry:
            if digits[ind] == 9:
                digits[ind]=0
                ind-=1
                if ind == -1:
                    digits.insert(0,1)
                    return digits
            else :
                digits[ind]+=1
                return digits



            
        
        