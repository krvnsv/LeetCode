class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]  # Pythonic way to reverse a string
    
if __name__ == "__main__":  # Only runs when you execute this file directly
    x = 121
    result = Solution().isPalindrome(x)
    print("Expected result: True")
    print("Result:", result)