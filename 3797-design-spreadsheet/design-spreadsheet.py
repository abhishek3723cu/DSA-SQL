class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26  # A-Z
        self.grid = {}  # store only set cells: (row, col) -> value

    def _parseCell(self, cell: str):
        """Convert cell like 'B10' -> (row=10, col=1)."""
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:])  # 1-indexed
        return (row, col)

    def setCell(self, cell: str, value: int) -> None:
        pos = self._parseCell(cell)
        self.grid[pos] = value

    def resetCell(self, cell: str) -> None:
        pos = self._parseCell(cell)
        if pos in self.grid:
            del self.grid[pos]

    def getValue(self, formula: str) -> int:
        # formula is "=X+Y"
        _, expr = formula[0], formula[1:]  # skip "="
        X, Y = expr.split("+")

        def resolve(token):
            if token.isdigit():  # number
                return int(token)
            row, col = self._parseCell(token)
            return self.grid.get((row, col), 0)

        return resolve(X) + resolve(Y)
