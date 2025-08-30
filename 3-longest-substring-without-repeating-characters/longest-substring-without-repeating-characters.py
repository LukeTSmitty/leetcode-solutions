class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        proposed solution steps:
        1. For every substring
        2. check if substring is valid
        3. update length of maxlen if valid
        """
        MAX_UNIQUE_SUBSTRING = 97
        max_len = 0
        # go over all possible substring lengths starting with the largest
        i = 0
        longest = 0
        
        #limits
        if len(s) > MAX_UNIQUE_SUBSTRING:
            longest = MAX_UNIQUE_SUBSTRING
        else:
            longest = len(s)

        for sub_len in range(longest, 0, -1):
            index = 0
            while (index + sub_len <= len(s)):
                substring = s[index:sub_len+index]
                index +=1
                flag = 0
                # Check if substring is valid
                for element in substring:
                    if(substring.count(element)>1):
                        flag = 1
                        break
                if flag == 0:
                    max_len = len(substring)
                    return max_len
       
        return max_len
                
            
        



            
            
            

            
        