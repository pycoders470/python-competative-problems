"""
Given two strings s and t, determine whether t is an anagram of s. Return true if they are anagrams, and false otherwise.
An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.
Example 1:
Input: s = "god", t = "dog"
Output: true
Example 2:
Input: s = "can", t = "pan"
Output: false

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams of each other.

        Pseudocode:
        1. Initialize: count = 0
        2. For each character i in string s:
           a. if i EXISTS in string t:
              - increment count
        3. if count == len(t):
           - return True (all characters match)
        4. Else:
           - return False (not anagrams)

        Approach:
        - Count how many characters from s exist in t
        - If all characters from s are found in t AND counts match, they're anagrams
        - An anagram uses ALL original letters exactly once

        Time Complexity: O(n × m) - n chars in s, for each check if in t (O(m))
        Space Complexity: O(1) - only uses counter variable

        Args:
            s (str): first string
            t (str): second string to compare

        Returns:
            bool: True if t is an anagram of s, False otherwise

        Example:
            >>> solution = Solution()
            >>> result = solution.isAnagram("god", "dog")
            >>> print(result)
            True  # "dog" is an anagram of "god"
        """
        count = 0
        for i in s:
            if i in t:
                count+=1 
        if count==len(t):
            return True
        return False


if __name__ == '__main__':
    print("=" * 50)
    print("Anagram Checker")
    print("=" * 50)
    
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("god", "dog", True),
        ("can", "pan", False),
        ("listen", "silent", True),
        ("hello", "world", False),
        ("abc", "cba", True),
        ("a", "a", True),
        ("ab", "ba", True),
        ("ab", "cd", False)
    ]
    
    print("\n--- Testing Anagram Detection ---")
    for s, t, expected in test_cases:
        result = solution.isAnagram(s, t)
        status = "✓" if result == expected else "✗"
        output = "Anagrams" if result else "Not Anagrams"
        print(f"{status} isAnagram('{s}', '{t}') = {output}")
    
    print("=" * 50)