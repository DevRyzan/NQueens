import sys
import os
import time
from decimal import Decimal


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from Factories.ManuelMethods.FasterDFSMethodFactory import FasterDFSMethodFactoryClass
from Factories.ManuelMethods.DFSMethodFactory import DFSMethodFactoryClass
from Factories.ManuelMethods.BFSMethodFactory import BFSMethodFactoryClass  
from Factories.GeneticAlgh.GeneticAlghFactory import GeneticAlghFactoryClass


class Main:
    @staticmethod
    def run():
        try:
            # Prompt the user for the size of the board
            n = int(input("Enter the number of queens: "))
            if n <= 0:
                print("Please enter a positive integer.")
                return

            # Display available solving methods
            print("\nChoose a method to solve the problem:")
            print("1. Faster DFS Method")
            print("2. Standard DFS")
            print("3. BFS")
            print("4. Genetic Algorithm")
            choice = int(input("Enter your choice (1, 2, 3, or 4): "))
 
            if choice == 1:
                solver = FasterDFSMethodFactoryClass(n)
                print("Using Faster DFS Method...")
            elif choice == 2:
                solver = DFSMethodFactoryClass(n)
                print("Using Standard DFS...")
            elif choice == 3:
                solver = BFSMethodFactoryClass(n)
                print("Using BFS...")
            elif choice == 4:
                population_size = int(input("Enter population size (default: 100): ") or 100)
                generations = int(input("Enter maximum generations (default: 500): ") or 500)
                mutation_rate = float(input("Enter mutation rate (default: 0.1): ") or 0.1)
                solver = GeneticAlghFactoryClass(n, population_size, generations, mutation_rate)
                print("Using Genetic Algorithm...")
            else:
                print("Invalid choice. Please select a valid option.")
                return

            print(f"\nExploring solutions for {n}-Queens problem...")
            start_time = time.time()
            total_solutions = solver.find_solutions()
            end_time = time.time()

            elapsed_time = Decimal(end_time - start_time)
            print(f"\nTotal valid solutions found: {total_solutions}")
            print(f"Execution time: {elapsed_time:.6f} seconds")

            if choice == 4:
                solver.display_solution()

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    Main.run()