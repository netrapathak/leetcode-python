class Solution:
    def romanToInt(self, s: str) -> int:
        dict_ = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M':1000}
        n = len(s) - 1
        num = dict_.get(s[n]) # need not check the last letter with next letter
        # for all letters except last
        # go upto second last to compare with last
        for i in range(0, n):
            num += int(dict_.get(s[i])) #add everything initially
            # specific check for letters rather than check for all letters to speed up
            if (s[i] == 'I' or s[i] == 'X' or s[i] == 'C'):
                if dict_.get(s[i+1]) > dict_.get(s[i]):
                    num -= 2 * dict_.get(s[i]) #subtract twice since once added before
                
        return num
            
        
