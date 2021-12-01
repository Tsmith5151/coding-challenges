"""
Find the smallest value in an integer array without sorting it.
"""


def smallestNumber(nums):
    """
    :type nums: List[int]
    :type n: int
    """
    _min = nums[0]
    for i in range(0, len(nums)):
        if nums[i] < _min:
            # replace number with smaller value
            _min = nums[i]
    print(f"Smallest Value: {_min}")


if __name__ == "__main__":
    nums = [5, 3, 1, 4, 7, 8, 5]
    print(smallestNumber(nums))
