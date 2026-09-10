class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        def helper(i, remain):
            if i == len(nums) - 1:
                return True

            if nums[i] <= nums[i + 1]:
                return helper(i + 1, remain)
            elif remain > 0:
                # change the first
                tmp = nums[i]
                nums[i] = nums[i + 1]
                if helper(i + 1, remain - 1):
                    nums[i] = tmp
                    return True
                nums[i] = tmp

                tmp = nums[i+1]
                nums[i + 1] = nums[i]
                if helper(i + 1, remain - 1):
                    nums[i+1] = tmp 
                    return True
                nums[i+1] = tmp

            return False


                
        return helper(0, 1)




        
