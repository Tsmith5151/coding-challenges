""" 
Longest Consecutive Sequence

Reference: https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Solution:
if we just sorted the array -> Time Complexity = O(nlogn)
Can we do better? -> Time Complexity = O(n)

Solution:
The start of each sequence has a left value
So check if the start of the sequence - 1 is in the set or not.
This will tell is if this is the start of the sequence or not.
If so, check to the right of the sequence + 1 to see if in the set.
If so, check how long the sequence is.
[1,2,3,4].....[100]....[200]
"""


def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    sequence = set(nums)
    results = 0

    if len(sequence) == 1:
        return 1

    for i in range(0, len(sequence)):
        seq = list(sequence)
        # check if start of sequence
        if seq[i] - 1 not in sequence:
            # Start of sequence
            if seq[i] + 1 in sequence:
                # Find the end of sequence
                length = 0
                while seq[i] + length in sequence:
                    length += 1
                # get max of sequence length
                results = max(results, length)
    return results


if __name__ == "__main__":
    sequence = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(sequence))
