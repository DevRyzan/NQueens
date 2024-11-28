import time
from collections import deque
from decimal import Decimal


class BFSMethodFactoryClass:
    def __init__(self, n):
        self.n = n
        self.solution_counter = Decimal(0)

    def is_safe(self, board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def bfs(self):
        queue = deque()
        queue.append((0, [-1] * self.n))

        while queue:
            row, board = queue.popleft()

            if row == self.n:
                self.solution_counter += 1
                continue

            for col in range(self.n):
                if self.is_safe(board, row, col):
                    new_board = board[:]
                    new_board[row] = col
                    queue.append((row + 1, new_board))

    def solve(self):
        self.bfs()
        return self.solution_counter

