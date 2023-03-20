from graph import Graph
from copy import deepcopy

#ovde cuvam permutaciju koja ima najbolji color_sum
best_permutation = []
best_coloring_sum = float('inf')
def free_colors(zauzete, ind, n):
    slobodne = []
    for i in range(1,n+1):
        if i not in zauzete[ind]:
            slobodne.append(i)
    return slobodne
def calc_sum_of_coloring(permutation, graph):
    n = graph.num_of_vertices
    x_boje = [0 for _ in range(n)]
    zauzete = [[] for _ in range(n)]

    for i in range(len(permutation)):
        ind = permutation.index(i)
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

    return sum(x_boje)
def next_permutation(permutation, i, used, graph):
# ako smo stigli do kraja generisali smo jednu permutaciju
    if i == len(permutation):
        coloring_sum = calc_sum_of_coloring(permutation, graph)
        global best_coloring_sum
        global best_permutation
        if coloring_sum < best_coloring_sum:
            best_coloring_sum = coloring_sum
            best_permutation = deepcopy(permutation)
    else:
        for j in range(0, len(permutation)):
            if used[j] == False:
                permutation[i] = j
                used[j] = True
                next_permutation(permutation, i+1,used, graph)
                used[j] = 0
def brute_force(graph):

    permutation = [0 for _ in range(graph.num_of_vertices)]
    used = [False for _ in range(graph.num_of_vertices)]
    next_permutation(permutation, 0, used, graph)
    global best_coloring_sum
    global best_permutation
    return best_permutation, best_coloring_sum

if __name__ == '__main__':
    g = Graph(12)
    g.random_graph()
    g.save_graph_to_file("small_random_graph.txt")
    g.load_graph_from_file("small_random_graph.txt")
    # print(g)
    # print(brute_force(g))