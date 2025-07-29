import array

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for i in range(0,len(nums)):
            if output:
                break

            x = nums[i]

            if (i+1 >= len(nums)):
                continue

            for j in range(i+1, len(nums)): 
                y = nums[j]

                if x+y == target:
                    output.append(i)
                    output.append(j)
                    break
        return output
            

        