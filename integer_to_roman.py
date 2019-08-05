class Solution:
    def intToRoman(self, num: int) -> str:       
        """
        :type num: int
        :rtype: str
        """
        dict_ = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        num_value = ""
        for k in dict_:
            while num >= k:
                num_value += dict_[k]
                num -= k
        return num_value
            
           
