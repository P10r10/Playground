class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for row in grid:
            for i in range(len(row) - 1, -1, -1):
                if row[i] < 0:
                    count += 1
                else:
                    break
        return count


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(Solution().countNegatives(grid))
