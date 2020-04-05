"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose
of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        x = list(x)
        x.reverse()
        if x[0] == '0':
            x.pop(0)
            if x[0] == '0':
                x.pop(0) 
        last_item = len(x) - 1
        if x[last_item] == '-':
            x.pop()
            x.insert(0, '-')
        result = ''
        for i in x: 
            result += i
        return result
# solution = Solution()
# print(solution.reverse(-123))          
