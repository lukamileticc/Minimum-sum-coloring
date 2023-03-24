import random

import numpy as np

from hybrid_ga_sa import hybrid
from simulated_annealing_msc import simulated_annealing
from local_search_mcs import local_search
from brute_force_msc import brute_force
from local_search_mcs import calc_solution_value
from genetic_algorithm_msc import ga
from VNS import vns
from graph import Graph

if __name__ == '__main__':
    g = Graph(10)
    g.random_graph()
    g.save_graph_to_file("our_graph_instances/random_graph.txt")
    g.load_graph_from_file("our_graph_instances/random_graph.txt")
    # print(g)
    max_iters = 10000
    random.seed(2314141)
    np.random.seed(2314141)

    #Brute force algorithm
    # solution, curr_value = brute_force(g)
    # print("Brute force results: ")
    # _,colors_vector = calc_solution_value(solution,g)
    # print(colors_vector)
    # print(curr_value)

    #Local search algorithm
    random.seed(2314141)
    np.random.seed(2314141)
    solution, curr_value = local_search(g, max_iters)
    print("Local search results: ")
    _,colors_vector = calc_solution_value(solution,g)
    print(colors_vector)
    print(curr_value)
    suma, _ = calc_solution_value(solution, g)
    print(suma)

    #Simulated annealing algorithm
    random.seed(2314141)
    np.random.seed(2314141)
    solution, curr_value = simulated_annealing(g, max_iters)
    print("Simulated_annealing results: ")
    _, colors_vector = calc_solution_value(solution, g)
    print(colors_vector)
    print(curr_value)
    suma, _ = calc_solution_value(solution, g)
    print(suma)

    #Variable Neighborhood Search (VNS)
    random.seed(2314141)
    np.random.seed(2314141)
    k_max = 5
    move_prob = 0.5
    solution, curr_value = vns(g,max_iters,k_max,move_prob)
    print("Variable Neighborhood Search (VNS) results: ")
    _, colors_vector = calc_solution_value(solution, g)
    print(colors_vector)
    print(curr_value)
    suma,_ = calc_solution_value(solution,g)
    print(suma)

    #Genetic algorithm
    # parametri genetski=og algoritma
    random.seed(2314141)
    np.random.seed(2314141)
    POPULATION_SIZE = 100
    NUM_OF_GENERATIONS = 100
    ELITISM_SIZE = POPULATION_SIZE // 5
    TOURNAMENT_SIZE = 10
    MUTATION_PROB = 0.05  # 5%
    solution, curr_value = ga(g,POPULATION_SIZE,NUM_OF_GENERATIONS,ELITISM_SIZE,TOURNAMENT_SIZE,MUTATION_PROB)
    print("Genetic algorithm results: ")
    _, colors_vector = calc_solution_value(solution, g)
    print(colors_vector)
    print(curr_value)
    suma, _ = calc_solution_value(solution, g)
    print(suma)

    # HYBRID algorithm
    random.seed(2314141)
    np.random.seed(2314141)
    solution, curr_value = hybrid(g,POPULATION_SIZE,NUM_OF_GENERATIONS,ELITISM_SIZE,TOURNAMENT_SIZE,MUTATION_PROB)
    print("Hybrid (ga + sa) results: ")
    _, colors_vector = calc_solution_value(solution, g)
    print(colors_vector)
    print(curr_value)
    suma, _ = calc_solution_value(solution, g)
    print(suma)