from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return (i, j)
                
# Test case

if __name__ == "__main__":  # Only runs when you execute this file directly
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)
    print("Expected result: (0 ,1)")
    print("Result:", result)