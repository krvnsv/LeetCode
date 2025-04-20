class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10 # integer (floor) division. output: 12

        # Step 3: Compare the first half and the second half
        # For odd length, we can disregard the middle digit, so we compare `x` and `reversed_half // 10`
        return x == reversed_half or x == reversed_half // 10
    
if __name__ == "__main__":  # Only runs when you execute this file directly
    x = 121
    result = Solution().isPalindrome(x)
    print("Input: ", x)
    print("Result:", result)