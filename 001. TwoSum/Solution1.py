class Solution:
    def twoSum(self, nums, target):
        x = 0
        y = len(nums) - 1
        while x < y:
            if nums[x] + nums[y] == target:
                return (x, y)
            if nums[x] + nums[y] < target:
                x += 1
            else:
                y -= 1
        self.x = x
        self.y = y
        self.array = array       
        return None

test_case = Solution()    
array = [1, 5, 7]