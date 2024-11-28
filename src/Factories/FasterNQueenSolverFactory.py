from decimal import Decimal

class FasterNQueenSolverClass:
    def __init__(self, n):
        self.n = n
        self.solution_counter = Decimal(0)  # Counter for solutions

    def solve(self, row, columns, diagonals1, diagonals2):
        if row == self.n:
            self.solution_counter += Decimal(1)
            return

        # Calculate all possible positions for the current row
        available_positions = ((1 << self.n) - 1) & ~(columns | diagonals1 | diagonals2)

        while available_positions:
            # Get the rightmost available position
            position = available_positions & -available_positions
            available_positions -= position

            # Recur to place the next queen
            self.solve(
                row + 1,
                columns | position,
                (diagonals1 | position) << 1,
                (diagonals2 | position) >> 1
            )

    def find_solutions(self):
        self.solve(0, 0, 0, 0)
        return self.solution_counter

