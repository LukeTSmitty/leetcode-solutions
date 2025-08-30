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
        characters = []
        # go over all possible substring lengths
        i = 0
        longest = 0
        
        #limits
        if len(s) > MAX_UNIQUE_SUBSTRING:
            longest = MAX_UNIQUE_SUBSTRING
        else:
            longest = len(s)

        while(len(characters) < MAX_UNIQUE_SUBSTRING and i < len(s)):
            char = s[i]
            i+=1
            if (char not in characters):
                characters.append(char)
                max_len = 1

        for sub_len in range(longest, 0, -1):
            index = 0
            while (index + sub_len <= len(s)):
                substring = s[index:sub_len+index]
                index +=1

                # Check if substring is valid
                flag = 0
                for element in characters:
                    if (substring.count(element) > 1):
                        flag = 1
                        break
                if (flag == 0):
                    #if it's valid update max length and check for maximum
                    max_len = len(substring)
                    return max_len
        return max_len
                
            
        



            
            
            

            
        