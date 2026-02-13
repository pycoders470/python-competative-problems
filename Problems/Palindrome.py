"""
Module: Palindrome
Purpose: Check if an integer is a palindrome by reversing and comparing
Complexity: O(log x) where x is the input number
"""

class Solution(object):
    """
    Check if an integer is a palindrome.
    A palindrome reads the same forwards and backwards.
    Negative numbers are not palindromes.
    """
    
    def isPalindrome(self, x: int) -> bool:
        """
        Check if integer x is a palindrome.
        Handles 32-bit integer constraints: -2^31 to 2^31 - 1
        
        Pseudocode:
            if x < 0: return False
            original = x
            reversed_num = 0
            while x > 0:
                reversed_num = reversed_num * 10 + x % 10
                x = x // 10
            return reversed_num == original
        
        Time Complexity: O(log x) - iterate through each digit
        Space Complexity: O(1)
        
        Args:
            x: Integer to check for palindrome property
        
        Returns:
            True if x is a palindrome, False otherwise
        
        Example:
            isPalindrome(121) → True
            isPalindrome(-121) → False
            isPalindrome(10) → False
            isPalindrome(0) → True
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Single digit numbers are palindromes
        if x < 10:
            return True
        
        original = x
        rev = 0
        minInt = -2**31
        maxInt = 2**31 - 1
        
        # Reverse the number
        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10
        
        # Check if reversed number is within 32-bit range
        if rev < minInt or rev > maxInt:
            return False
        
        # Compare with original
        return rev == original


if __name__ == '__main__':
    print("=" * 50)
    print("Palindrome Number Checker")
    print("=" * 50)
    
    solution = Solution()
    
    # Test cases
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (1, True),
        (12321, True),
        (1221, True),
        (1234, False),
        (9, True),
        (100, False)
    ]
    
    print("\n--- Testing Palindrome Check ---")
    for num, expected in test_cases:
        result = solution.isPalindrome(num)
        status = "✓" if result == expected else "✗"
        output = "Palindrome" if result else "Not Palindrome"
        print(f"{status} isPalindrome({num:6d}) = {output}")
    
    print("=" * 50)