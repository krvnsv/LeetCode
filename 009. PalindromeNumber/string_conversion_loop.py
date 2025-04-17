class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = ''

        for i in range(len(s) - 1, -1, -1):
            n = n + s[i]

        if s == n:
            return True
        else:
            return False
        
if __name__ == "__main__":  # Only runs when you execute this file directly
    x = 121
    result = Solution().isPalindrome(x)
    print("Expected result: True")
    print("Result:", result)