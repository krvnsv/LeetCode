from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

# Test case

if __name__ == "__main__":  # Only runs when you execute this file directly
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)
    print("Expected result: (0 ,1)")
    print("Result:", result)