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


# Define a function named get_nr_items that takes one parameter: user_input
def get_nr_items(user_input):
    # Split the user_input string by comma and store the resulting items in the 'items' list
    items = user_input.split(",")
    # Return the length of the 'items' list
    return len(items)


def calculate_time(
    h,
    g=9.80665,
):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)
