import sys
import os
import time
from decimal import Decimal


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from Factories.ManuelMethods.FasterDFSMethodFactory import FasterDFSMethodFactoryClass
from Factories.ManuelMethods.DFSMethodFactory import DFSMethodFactoryClass 
from Factories.GeneticAlgh.GeneticAlghFactory import GeneticAlghFactoryClass


class Main:
    @staticmethod
    def run():
        try:
            n = int(input("Enter the Queens number:"))
            if n <= 0:
                print("Please enter a positive value.")
                return

            print("\nChoose a SC to solve the problem:")
            print("1. Faster DFS SC")
            print("2. Standard DFS")
            print("3. BFS")
            print("4. Genetic Algorithm")
            choicenSC = int(input("Enter your choice (1, 2 or 3): "))
 
            if choicenSC == 1:
                solver = FasterDFSMethodFactoryClass(n)
                print("Using Faster DFS SC...")
            elif choicenSC == 2:
                solver = DFSMethodFactoryClass(n)
                print("Using Standard DFS SC...")
            elif choicenSC == 3:
                populationSize = int(input("Enter population size (default: 100): ") or 100)
                generations = int(input("Enter maximum generations (default: 500): ") or 500)
                mutationRate = float(input("Enter mutation rate (default: 0.1): ") or 0.1)
                solver = GeneticAlghFactoryClass(n, populationSize, generations, mutationRate)
                print("Using Genetic Algh..")
            else:
                print("Invalid choice.")
                return

            print(f"\nExploring solutions for {n}-Queens problem...")
            start_time = time.time()
            total_solutions = solver.find_solutions()
            end_time = time.time()

            elapsed_time = Decimal(end_time - start_time)
            print(f"\nTotal valid solutions found: {total_solutions}")
            print(f"Execution time: {elapsed_time:.6f} seconds")

            if choicenSC == 4:
                solver.display_solution()

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    Main.run()