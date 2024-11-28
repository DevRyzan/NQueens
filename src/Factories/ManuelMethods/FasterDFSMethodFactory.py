from decimal import Decimal

class FasterDFSMethodFactoryClass:
    def __init__(self, n):
        self.n = n
        self.solution_counter = Decimal(0)   

    def solve(self, row, columns, diagonals1, diagonals2):
        if row == self.n:
            self.solution_counter += Decimal(1)
            return

       
        available_positions = ((1 << self.n) - 1) & ~(columns | diagonals1 | diagonals2)

        while available_positions:
            
            position = available_positions & -available_positions
            available_positions -= position

            self.solve(
                row + 1,
                columns | position,
                (diagonals1 | position) << 1,
                (diagonals2 | position) >> 1
            )

    def find_solutions(self):
        self.solve(0, 0, 0, 0)
        return self.solution_counter

