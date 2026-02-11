"""
Grouping Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        Group anagrams together from a list of strings.

        Pseudocode:
        1. Initialize: output = {} (empty dictionary)
        2. For each string i in strs:
           a. sorted_str = sort characters in i alphabetically
           b. if sorted_str EXISTS as key in output:
              - append i to output[sorted_str]
           c. else:
              - create new list: output[sorted_str] = [i]
        3. Return all values (grouped anagrams) from dictionary

        Approach:
        - Anagrams have identical characters when sorted
        - Use sorted string as key to group anagrams
        - Dictionary automatically groups strings with same sorted form

        Time Complexity: O(n × k log k) - n strings, each sorted in O(k log k)
        Space Complexity: O(n) - dictionary stores all strings

        Args:
            strs (List[str]): list of strings to group

        Returns:
            List[List[str]]: grouped anagrams, each group in a list

        Example:
            >>> solution = Solution()
            >>> result = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
            >>> print(result)
            [["eat","tea","ate"], ["tan","nat"], ["bat"]]
            # Anagrams grouped together
        """
        output = {}
        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str in output:
                output[sorted_str].append(i)
            else:
                output[sorted_str] = [i]
        return list(output.values())
        