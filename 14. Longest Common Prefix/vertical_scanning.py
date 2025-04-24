from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the shortest string
        shortest = min(strs, key=len)

        # Check each character in the shortest string
        for i in range(len(shortest)):
            for word in strs:
                if word[i] != shortest[i]:
                    return shortest[:i]  # Return prefix up to this point
        return shortest  # All characters matched
