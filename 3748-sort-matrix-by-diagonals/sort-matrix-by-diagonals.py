class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = {}

        # Collect diagonals
        for i in range(n):
            for j in range(n):
                key = i - j
                if key not in diagonals:
                    diagonals[key] = []
                diagonals[key].append(grid[i][j])

        # Sort diagonals
        for key, values in diagonals.items():
            if key >= 0:  # bottom-left (including main diagonal)
                values.sort(reverse=True)
            else:  # top-right
                values.sort()
            diagonals[key] = values

        # Place back into grid
        for i in range(n):
            for j in range(n):
                key = i - j
                grid[i][j] = diagonals[key].pop(0)

        return grid
