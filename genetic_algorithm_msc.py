import random
from copy import deepcopy

import numpy as np
from matplotlib import pyplot as plt
from graph import Graph
from simulated_annealing_msc import calc_solution_value
def free_colors(zauzete, ind, n):
    slobodne = []
    for i in range(1,n+1):
        if i not in zauzete[ind]:
            slobodne.append(i)
    return slobodne

def initialize(num_of_alleles):
    #generisemo permutacije
    solution = list(np.random.permutation(num_of_alleles))
    return solution

def draw_graph(xs, ys):
    # iscrtavnanje grafika
    plt.title('Simulated annealing: Solution value through the iterations: ')
    plt.xlabel('Iters')
    plt.ylabel('Target function')
    plt.plot(xs, ys, color='blue')
    plt.show()


class Individual:
    def __init__(self, graph):
        # kod jedinke
        self.code = initialize(graph.num_of_vertices)

        # prilagodjenost jedinke
        self.fitness = self.calc_fitness(graph)

    def calc_fitness(self, graph):
        n = graph.num_of_vertices
        x_boje = [0 for _ in range(n)]
        zauzete = [[] for _ in range(n)]

        for i in range(len(self.code)):
            ind = self.code.index(i)
            if i == 0:
                x_boje[ind] = 1
                for j in range(n):
                    if graph.get_edges(ind, j) == 1:
                        zauzete[j].append(1)
            else:
                slobodne = free_colors(zauzete, ind, n)
                x_boje[ind] = min(slobodne)
                for j in range(n):
                    if graph.get_edges(ind, j) == 1:
                        zauzete[j].append(x_boje[ind])

        # print(x_boje)
        # print(sum(x_boje))
        # return sum(x_boje), x_boje

        fitness = 1 / sum(x_boje)
        return fitness

    def __lt__(self, other):
        return self.fitness < other.fitness

def tournament_selection(population, tournament_size,graph, forbiden=None):
    allowed = list(set(population).difference({forbiden}))
    random_individulas = random.sample(allowed,tournament_size)
    #potrebno je da nadjemo najbolju po fitnesu
    best_individual = Individual(graph)
    best_fitness = 0
    for individual in random_individulas:
        if individual.fitness > best_fitness:
            best_fitness = individual.fitness
            best_individual = individual
    return best_individual

def roulette_selection(population):
    # racunamo fitness cele populacije
    population_fitness = sum([individual.fitness for individual in population if individual.fitness != float('-inf')])

    # racunamo verovatnoce svake jedinke
    # na osnovu fitnessa
    individual_prob = [individual.fitness / population_fitness for individual in population]

    return np.random.choice(population, replace=False, p=individual_prob)
    # ovako ne moze
    # return np.choice(population,p = individual_prob)

#Ukrstanje prvog reda kod permutacijama
def crossover(parent1, parent2,child1,child2):

    c1_code = deepcopy(child1.code)
    c2_code = deepcopy(child2.code)

    start_pos,end_pos = sorted(random.sample(range(len(parent1.code)),2))
    c1_code = [-1] * len(parent1.code)
    c1_code[start_pos:end_pos] = parent1.code[start_pos:end_pos]

    for i in range(len(c1_code)):
        if c1_code[i] == -1:
            for j in range(len(parent2.code)):
                if parent2.code[j] not in c1_code:
                    c1_code[i] = parent2.code[j]
                    break



    c2_code = [-1] * len(parent2.code)
    c2_code[start_pos:end_pos] = parent1.code[start_pos:end_pos]

    for i in range(len(c2_code)):
        if c2_code[i] == -1:
            for j in range(len(parent1.code)):
                if parent1.code[j] not in c2_code:
                    c2_code[i] = parent1.code[j]
                    break

    child1.code = c1_code
    child2.code = c2_code

#Mutacija zasnovana na zameni
def mutation(individual,MUTATION_PROB):
    poz1 = random.randrange(0, len(individual.code))
    poz2 = random.randrange(0, len(individual.code))
    pom = individual.code[poz1]
    individual.code[poz1] = individual.code[poz2]
    individual.code[poz2] = pom

#Mutacija zasnovana na mesanju
def mutation_better(individual):

    start_pos,end_pos = sorted(random.sample(range(len(individual.code)),2))
    new_code = individual.code[start_pos:end_pos+1]
    #shuffle in place
    random.shuffle(new_code)
    individual.code[start_pos:end_pos+1] = new_code

def ga(graph,POPULATION_SIZE, NUM_OF_GENERATIONS, ELITISM_SIZE,TOURNAMENT_SIZE,MUTATION_PROB):
    # pravim populaciju
    population = [Individual(graph) for _ in range(POPULATION_SIZE)]
    new_population = [Individual(graph) for _ in range(POPULATION_SIZE)]

    #za crtanje
    xs = []
    ys = []

    for i in range(NUM_OF_GENERATIONS):
        # izdavajamo najbolje-moramo sortirati
        population.sort(key=lambda x: x.fitness, reverse=True)
        # kopiramo najbolje
        new_population[:ELITISM_SIZE] = population[:ELITISM_SIZE]

        # ostale jedinke ukrstamo
        for j in range(ELITISM_SIZE, POPULATION_SIZE, 2):
            # parent1 = tournament_selection(population,TOURNAMENT_SIZE)
            # parent2 = tournament_selection(population,TOURNAMENT_SIZE,forbiden = parent1)

            parent1 = roulette_selection(population)
            parent2 = roulette_selection(population)

            choices = {chromosome: chromosome.fitness for chromosome in population}

            crossover(parent1,
                      parent2,
                      new_population[j],
                      new_population[j + 1])
            mut_allowed = random.uniform(0,1)
            if mut_allowed < MUTATION_PROB:
                # mutation(new_population[j], MUTATION_PROB)
                # mutation(new_population[j + 1], MUTATION_PROB)
                mutation_better(new_population[j])
                mutation_better(new_population[j + 1])

            new_population[j].fitness = new_population[j].calc_fitness(graph)
            new_population[j + 1].fitness = new_population[j + 1].calc_fitness(graph)

        xs.append(i)
        ys.append(1.0 / max(population).fitness)

        # poboljsavamo malo najbolju jedinku
        # simulated_annealing(new_population[0], iters=100)

        population = new_population

    #iscrtavanje grafika
    draw_graph(xs,ys)
    best_individual = max(population)
    # print(best_individual.code)
    # print(best_individual.fitness)
    # print(1.0 / best_individual.fitness)

    return best_individual.code , 1.0 / best_individual.fitness

if __name__ == '__main__':
    # parametri genetskog algoritma
    POPULATION_SIZE = 100
    NUM_OF_GENERATIONS = 100
    ELITISM_SIZE = POPULATION_SIZE // 5
    TOURNAMENT_SIZE = 5
    MUTATION_PROB = 0.05  # 5%

    # #pravimo graf
    g = Graph(60)
    g.random_graph()
    g.save_graph_to_file("random_graph.txt")
    g.load_graph_from_file("random_graph.txt")
    # # print(g)
    #
    # solution, curr_value = ga(g,POPULATION_SIZE,NUM_OF_GENERATIONS,ELITISM_SIZE,TOURNAMENT_SIZE,MUTATION_PROB)
    # print("#########")
    # print(solution)
    # print(curr_value)
    # suma,_ = calc_solution_value(solution,g)
    # print(suma)
