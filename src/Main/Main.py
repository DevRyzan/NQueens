import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from Factories.FasterNQueenSolverFactory import FasterNQueenSolverClass
import time
from decimal import Decimal
5

class Main:
    @staticmethod
    def run():
        try:
            n = int(input("Enter the number of queens: "))
            if n <= 0:
                print("Please enter a positive integer.")
                return

            # Solve the N-Queens problem
            solver = FasterNQueenSolverClass(n)
            print(f"Exploring solutions for {n}-Queens problem...")

            # Measure execution time
            start_time = time.time()
            total_solutions = solver.find_solutions()
            end_time = time.time()

            # Calculate elapsed time and operations per second
            elapsed_time = Decimal(end_time - start_time)  # Convert to Decimal
            solutions_per_second = total_solutions / elapsed_time if elapsed_time > 0 else Decimal(0)

            # Display results
            print(f"Total valid solutions found: {total_solutions}")
            print(f"Execution time: {elapsed_time:.6f} seconds")
            print(f"Solutions per second: {solutions_per_second:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Entry point
if __name__ == "__main__":
    Main.run()