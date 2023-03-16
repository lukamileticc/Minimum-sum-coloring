from simulated_annealing_msc import simulated_annealing
from local_search_mcs import local_search
from brute_force_msc import brute_force
from local_search_mcs import calc_solution_value
from graph import Graph

if __name__ == '__main__':
    g = Graph()
    g.load_graph_from_file("small_random_graph.txt")
    # print(g)
    max_iters = 10000

    #Brute force algorithm
    print("Brute force results: ")
    brute_force(g)

    #Local search algorithm
    solution, curr_value = local_search(g, max_iters)
    print("Local search results: ")
    _,colors_vector = calc_solution_value(solution,g)
    print(colors_vector)
    print(curr_value)

    #Simulated annealing algorithm
    solution, curr_value = simulated_annealing(g, max_iters)
    print("Simulated_annealing results: ")
    _, colors_vector = calc_solution_value(solution, g)
    print(colors_vector)
    print(curr_value)