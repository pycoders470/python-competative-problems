"""
Module: GCD
Purpose: Find Greatest Common Divisor (GCD) and Least Common Multiple (LCM) using multiple approaches
Complexity: O(min(m,n)) brute force, O(log min(m,n)) Euclidean algorithm
"""

def GCDorHCF(m: int, n: int) -> int:
    """
    Find GCD using Brute Force approach.
    Iterates from 1 to min(m,n) and finds largest common divisor.
    
    Pseudocode:
        if m == n: return n
        if n == 0 or m == 0: return max(m,n)
        gcd = 1
        for i in range(1, min(m,n)+1):
            if m % i == 0 AND n % i == 0:
                gcd = i
        return gcd
    
    Time Complexity: O(min(m,n)) - iterate through all numbers
    Space Complexity: O(1)
    
    Args:
        m: First integer
        n: Second integer
    
    Returns:
        Greatest Common Divisor of m and n
    
    Example:
        GCDorHCF(6, 9) → 3
        GCDorHCF(12, 18) → 6
    """
    if m == n:
        return n
    if n == 0 or m == 0:
        return max(m, n)
    gcd = 1
    for i in range(1, min(m, n) + 1):
        if (m % i == 0 and n % i == 0):
            gcd = i
    return gcd


def GCDwithoutRecursion(m: int, n: int) -> int:
    """
    Find GCD using Euclidean Algorithm (Iterative).
    Repeatedly applies: GCD(m,n) = GCD(n, m%n) until remainder is 0.
    
    Pseudocode:
        while m > 0 AND n > 0:
            if m > n:
                m = m % n
            else:
                n = n % m
        return (m == 0) ? n : m
    
    Time Complexity: O(log min(m,n)) - logarithmic convergence
    Space Complexity: O(1)
    
    Args:
        m: First integer
        n: Second integer
    
    Returns:
        Greatest Common Divisor of m and n
    
    Example:
        GCDwithoutRecursion(6, 9) → 3
        GCDwithoutRecursion(48, 18) → 6
    """
    while (m > 0 and n > 0):
        if m > n:
            m = m % n
        else:
            n = n % m
    return n if m == 0 else m


def GCDviaRecursion(m: int, n: int) -> int:
    """
    Find GCD using Euclidean Algorithm (Recursive).
    Base case: when n=0, return m. Recursive: return GCD(n, m%n).
    
    Pseudocode:
        if n == 0:
            return m
        return GCD(n, m % n)
    
    Time Complexity: O(log min(m,n)) - logarithmic convergence
    Space Complexity: O(log min(m,n)) - recursion call stack
    
    Args:
        m: First integer
        n: Second integer
    
    Returns:
        Greatest Common Divisor of m and n
    
    Example:
        GCDviaRecursion(6, 9) → 3
        GCDviaRecursion(12, 18) → 6
    """
    if n == 0:
        return m
    return GCDviaRecursion(n, m % n)


def LCM(a: int, b: int) -> int:
    """
    Find Least Common Multiple using GCD.
    Formula: LCM(a,b) = (a * b) / GCD(a,b)
    
    Pseudocode:
        gcd = GCDviaRecursion(a, b)
        lcm = (a * b) / gcd
        return lcm
    
    Time Complexity: O(log min(a,b)) - GCD calculation
    Space Complexity: O(log min(a,b)) - recursion call stack
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        Least Common Multiple of a and b
    
    Example:
        LCM(20, 14) → 140
        LCM(4, 6) → 12
    """
    gcd = GCDviaRecursion(a, b)
    lcm = (a * b) // gcd
    return lcm


if __name__ == '__main__':
    print("=" * 50)
    print("GCD & LCM Calculator")
    print("=" * 50)
    
    # Test cases
    test_pairs = [(6, 9), (12, 18), (48, 18), (100, 50)]
    
    print("\n--- Brute Force GCD ---")
    for m, n in test_pairs:
        result = GCDorHCF(m, n)
        print(f"GCDorHCF({m}, {n}) = {result}")
    
    print("\n--- Euclidean Iterative ---")
    for m, n in test_pairs:
        result = GCDwithoutRecursion(m, n)
        print(f"GCDwithoutRecursion({m}, {n}) = {result}")
    
    print("\n--- Euclidean Recursive ---")
    for m, n in test_pairs:
        result = GCDviaRecursion(m, n)
        print(f"GCDviaRecursion({m}, {n}) = {result}")
    
    print("\n--- LCM Calculation ---")
    lcm_pairs = [(20, 14), (4, 6), (12, 18)]
    for a, b in lcm_pairs:
        result = LCM(a, b)
        print(f"LCM({a}, {b}) = {result}")
    
    print("=" * 50)