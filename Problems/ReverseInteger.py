"""
Module: ReverseInteger
Purpose: Reverse an integer while handling 32-bit constraints
Complexity: O(log x) where x is the input number
"""

class Solution(object):
    """
    Reverse an integer given 32-bit signed integer constraints.
    Handles overflow/underflow by returning 0 if result exceeds bounds.
    """
    
    def reverse(self, x: int) -> int:
        """
        Reverse digits of a 32-bit signed integer.
        Return 0 if reversed integer overflows/underflows (-2^31 to 2^31 - 1).
        
        Pseudocode:
            sign = 1 if x > 0 else -1
            x = abs(x)
            reversed_num = 0
            while x != 0:
                digit = x % 10
                reversed_num = reversed_num * 10 + digit
                x = x // 10
            if reversed_num > 2^31 - 1:
                return 0
            return sign * reversed_num
        
        Time Complexity: O(log x) - iterate through each digit
        Space Complexity: O(1)
        
        Args:
            x: Integer to reverse (32-bit signed)
        
        Returns:
            Reversed integer, or 0 if overflow/underflow occurs
        
        Example:
            reverse(123) → 321
            reverse(-123) → -321
            reverse(120) → 21
            reverse(0) → 0
            reverse(1534236469) → 0 (overflow)
        """
        revnum = 0
        minInt = -2**31
        maxInt = 2**31 - 1
        
        # Preserve sign and work with absolute value
        sign = 1 if x > 0 else -1
        x = abs(x)
        
        # Reverse the digits
        while x != 0:
            digit = x % 10
            revnum = revnum * 10 + digit
            x = x // 10
        
        # Check for overflow/underflow
        if revnum < minInt or revnum > maxInt:
            return 0
        
        # Apply sign and return
        return sign * revnum


if __name__ == '__main__':
    print("=" * 50)
    print("Integer Reversal (32-bit Constraints)")
    print("=" * 50)
    
    solution = Solution()
    
    # Test cases
    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),  # Overflow case
        (-2147483648, 0), # Min 32-bit overflow
        (100, 1),
        (1000, 1),
        (7, 7),
        (-7, -7)
    ]
    
    print("\n--- Testing Integer Reversal ---")
    for num, expected in test_cases:
        result = solution.reverse(num)
        status = "✓" if result == expected else "✗"
        expected_str = "overflow" if expected == 0 and num != 0 else str(expected)
        print(f"{status} reverse({num:12d}) = {result:12d} (expected: {expected_str})")
    
    print("=" * 50)

