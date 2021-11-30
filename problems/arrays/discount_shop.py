"""
Final Prices With a Special Discount in a Shop

Reference: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.

Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation: 
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4. 
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2. 
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4. 
For items 3 and 4 you will not receive any discount at all.

Input: prices = [1,2,3,4,5]
Output: [1,2,3,4,5]
Explanation: In this case, for all items, you will not receive any discount at all.

Solution: iterate through the list and find the minimum price that is greater than the current price.
Time: O(n * m) where n is the length of the list and m is the length of the prices list.
"""


def finalPrices(prices):
    """
    :type prices: List[int]
    :rtype: List[int]
    """
    myList = []
    for i in range(len(prices) - 1):
        for j in prices[i + 1 :]:
            if prices[i] >= j:
                price = prices[i] - j
                break
            else:
                price = prices[i]
        myList.append(price)
    return myList + prices[-1:]


if __name__ == "__main__":
    prices = [8, 4, 6, 2, 3]
    print(finalPrices(prices))
