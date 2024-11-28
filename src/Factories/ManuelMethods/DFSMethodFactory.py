import time
from collections import deque
from decimal import Decimal


class DFSMethodFactoryClass:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solution_counter = 0  
    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i >= 0 and j < self.n:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve(self, row):
        if row == self.n:
            self.solution_counter += 1
            print(f"Solution {self.solution_counter}:")
            for r in self.board:
                print("".join("Q" if cell == 1 else "." for cell in r))
            print()
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve(row + 1)
                self.board[row][col] = 0

    def find_solutions(self):
        self.solve(0)
        return self.solution_counter  
