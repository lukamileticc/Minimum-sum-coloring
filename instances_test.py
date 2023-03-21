import random
import numpy as np

from VNS import vns
from graph import Graph
from local_search_mcs import local_search
from simulated_annealing_msc import simulated_annealing

if __name__ == '__main__':
    g = Graph()
    g.load_dimacs_file('graph_instances/group_1/mug88_25.txt')
    # print(g)
    iteration_number = 5
    best_value = float('inf')
    avg_value = 0



    max_iters = 10000
    random.seed(2314141)
    np.random.seed(2314141)

    for i in range(iteration_number):
        _, curr_value = vns(g, max_iters,5,0.5)
        avg_value += curr_value
        if curr_value < best_value:
            best_value = curr_value

    print("Simulated annealing results: ")
    print("Best value: " + str(best_value))
    print("Avg value: " + str(avg_value / iteration_number))
