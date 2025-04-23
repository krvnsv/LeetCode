from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range (1, n + 1):
            count = 0
            x = i
            while x > 0:
                count += x % 2
                x = x // 2
            ans.append(count)
        return ans