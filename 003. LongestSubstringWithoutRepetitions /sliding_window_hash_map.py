class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}  # Dictionary to store the most recent index of each character
        start = 0  # Start of the current substring
        max_length = 0  # Length of the longest substring without repeating characters
        
        for i, char in enumerate(s):
            if char in seen and seen[char] >= start:
                # If char is seen and its last occurrence is within the current window,
                # move start to the position after the last occurrence
                start = seen[char] + 1
            else:
                # Update max_length if the current substring is longer
                max_length = max(max_length, i - start + 1)
            
            # Update the most recent index of char
            seen[char] = i
        
        return max_length