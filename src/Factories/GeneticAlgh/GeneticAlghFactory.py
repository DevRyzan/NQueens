import random
from decimal import Decimal

class GeneticAlghFactoryClass:
    def __init__(self, n, population_size=500, generations=5000, mutation_rate=0.1):
        self.n = n
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.population = []
        self.solution_found = False
        self.best_solution = None

    def initialize_population(self):
        self.population = [[random.randint(0, self.n - 1) for _ in range(self.n)] for _ in range(self.population_size)]

    def fitness(self, board):
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        return -conflicts  # Lower conflicts = higher fitness

    def selection(self):
        def tournament():
            competitors = random.sample(self.population, k=5)
            return max(competitors, key=self.fitness)

        return tournament(), tournament()

    def crossover(self, parent1, parent2):
        split = random.randint(0, self.n - 1)
        child = parent1[:split] + parent2[split:]
        return child

    def mutate(self, board, generation):
        adaptive_rate = self.mutation_rate + (generation / self.generations) * 0.1
        if random.random() < adaptive_rate:
            row = random.randint(0, self.n - 1)
            board[row] = random.randint(0, self.n - 1)

    def introduce_diversity(self):
        num_new_individuals = self.population_size // 5
        new_individuals = [[random.randint(0, self.n - 1) for _ in range(self.n)] for _ in range(num_new_individuals)]
        self.population[-num_new_individuals:] = new_individuals

    def evolve(self, generation):
        new_population = []
        for _ in range(self.population_size):
            parent1, parent2 = self.selection()
            child = self.crossover(parent1, parent2)
            self.mutate(child, generation)
            new_population.append(child)
        self.population = new_population

    def find_solutions(self):
        self.initialize_population()

        for generation in range(self.generations):
            best_fitness = max(self.fitness(board) for board in self.population)
            print(f"Generation {generation}: Best fitness = {best_fitness}")
            
            for board in self.population:
                if self.fitness(board) == 0:
                    self.solution_found = True
                    self.best_solution = board
                    return Decimal(1)

            if generation % 100 == 0:  # Introduce diversity every 100 generations
                self.introduce_diversity()

            self.evolve(generation)

        return Decimal(0)

    def display_solution(self):
        if self.best_solution:
            print(f"Best solution: {self.best_solution}")
            for i in range(self.n):
                row = ["."] * self.n
                row[self.best_solution[i]] = "Q"
                print(" ".join(row))
        else:
            print("No valid solution found.")