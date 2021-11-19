"""
Asteroid Colliision

Reference: https://leetcode.com/problems/asteroid-collision/

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Solution: stacks
time complexity: O(n)

Reference: https://www.youtube.com/watch?v=LN7KjRszjk4
"""


def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """
    stack = []
    for a in asteroids:
        # case for collisions
        while stack and a < 0 and stack[-1] > 0:
            # case where a is larger than stack[-1]
            if a + stack[-1] < 0:
                stack.pop()
            # case where a i smaller than stack[-1]
            elif a + stack[-1] > 0:
                a = 0
            # case where a equals stack[-1]; destroy both
            else:
                a = 0
                stack.pop()
        if a != 0:
            stack.append(a)
    return stack


if __name__ == "__main__":
    asteroids = [5, 10, -5]
    print(asteroidCollision(asteroids))
