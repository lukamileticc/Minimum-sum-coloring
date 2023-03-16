from simulated_annealing_msc import simulated_annealing
from local_search_mcs import local_search
from graph import Graph

if __name__ == '__main__':
    g = Graph()
    g.load_graph_from_file("random_graph.txt")
    # print(g)
    max_iters = 10000


    solution, curr_value = local_search(g, max_iters)
    print("Local search results: ")
    print(solution)
    print(curr_value)

    solution, curr_value = simulated_annealing(g, max_iters)
    print("Simulated_annealing results: ")
    print(solution)
    print(curr_value)