class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        leng = len(nums) -1
        while x < leng:
            if nums[x] == nums[x+1]:
                del nums[x]
                leng = leng -1
            else:
                x = x+1
        return len(nums)
                
                
        