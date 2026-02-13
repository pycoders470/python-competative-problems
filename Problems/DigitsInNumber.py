"""
Module: DigitsInNumber
Purpose: Count digits in a number and check for Armstrong numbers
Complexity: O(log n) for both functions
"""

def digitsInNumber(n: int) -> int:
    """
    Count the number of digits in a given number.
    
    Pseudocode:
        count = 0
        while n != 0:
            digit = n % 10
            n = n // 10
            count += 1
        return count
    
    Time Complexity: O(log n) - dividing by 10 each iteration
    Space Complexity: O(1)
    
    Args:
        n: A positive integer
    
    Returns:
        Number of digits in n
    
    Example:
        digitsInNumber(3476888) → 7
        digitsInNumber(123) → 3
    """
    count = 0
    while n != 0:
        digit = n % 10
        n = n // 10
        count += 1
    return count


def ArmstrongNum(n: int) -> bool:
    """
    Check if a number is an Armstrong number (Narcissistic number).
    An Armstrong number is equal to the sum of its digits each raised to the power of digit count.
    Example: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
    
    Pseudocode:
        cube_sum = 0
        original = n
        while n != 0:
            digit = n % 10
            n = n // 10
            cube_sum += digit ^ 3
        return original == cube_sum
    
    Time Complexity: O(log n) - iterating through each digit
    Space Complexity: O(1)
    
    Args:
        n: A positive integer
    
    Returns:
        True if n is Armstrong number, False otherwise
    
    Example:
        ArmstrongNum(153) → True  (1³ + 5³ + 3³ = 153)
        ArmstrongNum(370) → True  (3³ + 7³ + 0³ = 370)
        ArmstrongNum(100) → False
    """
    cube = 0
    original = n
    while n != 0:
        digit = n % 10
        n = n // 10
        cube += digit ** 3
    return original == cube


if __name__ == '__main__':
    print("=" * 50)
    print("Digits in Number & Armstrong Number Checker")
    print("=" * 50)
    
    # Test digitsInNumber
    print("\n--- Count Digits ---")
    test_numbers = [3476888, 123, 1, 1000]
    for num in test_numbers:
        result = digitsInNumber(num)
        print(f"digitsInNumber({num}) = {result}")
    
    # Test Armstrong number
    print("\n--- Armstrong Numbers ---")
    armstrong_tests = [153, 370, 371, 407, 100, 111]
    for num in armstrong_tests:
        result = ArmstrongNum(num)
        status = "✓ Armstrong" if result else "✗ Not Armstrong"
        print(f"ArmstrongNum({num}) = {status}")
    
    print("=" * 50)