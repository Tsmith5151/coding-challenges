"""
Shuffle the Array

Link: https://leetcode.com/problems/shuffle-the-array/

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 

Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
"""

# Alternative solution
def shuffle1(nums, n):
    """
    :type nums: List[int]
    :type n: int
    """
    myList = []
    for i in list(zip(nums[:n], nums[n:])):
        myList.extend(i)
    return myList


def shuffle2(nums, n):
    """
    :type nums: List[int]
    :type n: int
    """
    myList = []
    for idx in range(len(nums)):
        if idx < n:
            myList.append(nums[idx])
            myList.append(nums[idx + n])
        else:
            return myList


if __name__ == "__main__":
    print(shuffle1([2, 5, 1, 3, 4, 7], n=3))
    print(shuffle2([2, 5, 1, 3, 4, 7], n=3))
