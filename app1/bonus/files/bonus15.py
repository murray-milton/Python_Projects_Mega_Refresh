class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # This acts as our memory of numbers we've seen so far.
        values = {}

        # Loop through the list, getting both the index (i) and the number (num)
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in values:
                return [values[remaining], i]
            # If no, add the current number to memory and keep going.
            # We store the number as the Key, and the index as the Value.
            values[num] = i
        return None


print(Solution().twoSum([2, 7, 11, 15], 9))
