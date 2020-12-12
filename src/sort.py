def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    red, white, blue = 0, 0, 0
    for i in nums:
        if i == 0:
            red += 1
        elif i == 1:
            white += 1
        elif i == 2:
            blue += 1

    nums[:] = [0] * red + [1] * white + [2] * blue
    return nums

def restoreString(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    encode = {i: str(s[idx]) for idx, i in enumerate(indices)}
    string = "".join([encode[i] for i in range(0, len(indices))])
    return string
