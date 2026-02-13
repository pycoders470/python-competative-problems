"""
Module: IsPrime
Purpose: Check if a number is prime and count primes up to n using multiple approaches
Complexity: O(√n) basic check, O(n² log n) brute force counting, O(n log log n) Sieve of Eratosthenes
"""

def isprime(n: int) -> bool:
    """
    Check if a number is prime using optimized trial division.
    A prime number is only divisible by 1 and itself.
    
    Pseudocode:
        if n < 2:
            return False
        for i in range(2, √n + 1):
            if n % i == 0:
                return False
        return True
    
    Time Complexity: O(√n) - check divisors up to square root
    Space Complexity: O(1)
    
    Args:
        n: Integer to check for primality
    
    Returns:
        True if n is prime, False otherwise
    
    Example:
        isprime(7) → True
        isprime(4) → False
        isprime(1) → False
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


class SolutionBruteForce(object):
    """
    Count all prime numbers up to n using Brute Force.
    Check each number individually for primality.
    """
    
    def countPrimes(self, n: int) -> int:
        """
        Count primes less than n using nested loops (Brute Force).
        
        Pseudocode:
            count = 0
            for i in range(2, n):
                is_prime = True
                for j in range(2, i//2 + 1):
                    if i % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    count += 1
            return count
        
        Time Complexity: O(n² log n) - nested loops with trial division
        Space Complexity: O(1)
        
        Args:
            n: Upper limit (exclusive)
        
        Returns:
            Count of prime numbers less than n
        
        Example:
            countPrimes(10) → 4 (primes: 2,3,5,7)
        """
        count = 0
        for i in range(2, n):
            is_prime = True
            for j in range(2, (i // 2) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
        return count


class SolutionSieveOfEratosthenes(object):
    """
    Count all prime numbers up to n using Sieve of Eratosthenes.
    Most efficient algorithm for finding all primes up to a given number.
    """
    
    def countPrimes(self, n: int) -> int:
        """
        Count primes less than n using Sieve of Eratosthenes.
        Mark all multiples of each prime as composite.
        
        Pseudocode:
            if n < 2: return 0
            is_prime = [True] * n
            is_prime[0] = is_prime[1] = False
            for i in range(2, √n + 1):
                if is_prime[i]:
                    for j in range(i², n, i):
                        is_prime[j] = False
            return count of True values in is_prime
        
        Time Complexity: O(n log log n) - most efficient
        Space Complexity: O(n) - boolean array
        
        Args:
            n: Upper limit (exclusive)
        
        Returns:
            Count of prime numbers less than n
        
        Example:
            countPrimes(10) → 4 (primes: 2,3,5,7)
        """
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return sum(is_prime)


if __name__ == '__main__':
    print("=" * 50)
    print("Prime Number Checker & Counter")
    print("=" * 50)
    
    # Test isprime function
    print("\n--- Check Individual Primes ---")
    test_numbers = [3, 4, 5, 6, 7, 8, 11, 12, 13, 15, 17]
    for num in test_numbers:
        result = isprime(num)
        status = "✓ Prime" if result else "✗ Not Prime"
        print(f"{num:2d} is {status}")
    
    # Test countPrimes Brute Force
    print("\n--- Count Primes (Brute Force) ---")
    brute = SolutionBruteForce()
    limits = [10, 20, 30]
    for limit in limits:
        result = brute.countPrimes(limit)
        print(f"Primes less than {limit}: {result}")
    
    # Test countPrimes Sieve
    print("\n--- Count Primes (Sieve of Eratosthenes) ---")
    sieve = SolutionSieveOfEratosthenes()
    for limit in limits:
        result = sieve.countPrimes(limit)
        print(f"Primes less than {limit}: {result}")
    
    print("=" * 50)
        return count