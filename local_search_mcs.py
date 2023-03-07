#!/usr/bin/python3
import random
import numpy as np
class Graph():

    def __init__(self,num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.adjacency_matrix = np.array([[0 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)])

        self.coloring_vector = []
    #neusmeren graf
    def add_edge(self, u, v):
        self.adjacency_matrix[u][v] = 1
        self.adjacency_matrix[v][u] = 1

    #ispis random grafa
    def random_graph(self):
        n = self.num_of_vertices
        self.adjacency_matrix = np.random.randint(0,2,(n,n))
        for i in range(n):
            for j in range(n):
                if self.adjacency_matrix[i][j] == 1:
                    self.adjacency_matrix[j][i] = 1
    def __str__(self):
       return str(self.adjacency_matrix)



def assign_color(graph):
    # vector of color
    #random bojenje
    # self.coloring_vector = np.array([np.random.randint(0,self.num_of_vertices) for _ in range(self.num_of_vertices)])
    #razlicito bojenje
    graph.coloring_vector = np.array([i for i in range(graph.num_of_vertices)])

# to check current coloring is valid or not
def is_coloring_valid(graph):
    for vertex,color in enumerate(graph.coloring_vector):
        for i in  range(graph.num_of_vertices):
            if graph.adjacency_matrix[vertex][i] == 1 and color == graph.coloring_vector[i]:
                return False
    return True

def calc_solution_value(graph):
    total = 0
    cost = 1
    k = max(graph.coloring_vector)
    for i in range(0,k+1):
        value = 0
        for color in graph.coloring_vector:
            if color == i:
                value += 1
        total += cost * value
        if value != 0:
            cost += 1
    return total

def change_coloring_vector(graph):
    random_vertex = random.randint(0,graph.num_of_vertices-1)
    #uzimamo boju 1. suseda
    for i in range(graph.num_of_vertices):
        if graph.adjacency_matrix[random_vertex][i] == 1:
            color = graph.coloring_vector[i]
            break

    #pamtimo staro_bojenje
    old_coloring = graph.coloring_vector.copy()
    #svim ostalim susedima stavljam tu boju
    for i in range(graph.num_of_vertices):
        if graph.adjacency_matrix[random_vertex][i] == 1:
            graph.coloring_vector[i] = color

    #proveravam da li je validno_menjanje
    if is_coloring_valid(graph):
        return True,old_coloring
    else:
        return False,old_coloring
def local_search(graph,iters):
    #initialize color
    assign_color(graph)
    curr_value = calc_solution_value(graph)
    best_value = curr_value


    for i in range(iters):
        #menjamo resenje
        # promeni_resenje
        # ako je nedopustivo , vrati na prethodno i nastavi dalje
        success,old_coloring = change_coloring_vector(graph)
        if not success:
            graph.coloring_vector = old_coloring.copy()
            continue
        new_value = calc_solution_value(graph)
        if new_value < curr_value:
            curr_value = new_value
            if new_value < best_value:
                best_value = curr_value
        else:
            #nastavi sa starim resenjem
            graph.coloring_vector = old_coloring

    return best_value


def simulated_annealing(graph, iters):
    # initialize color
    assign_color(graph)
    curr_value = calc_solution_value(graph)
    best_value = curr_value

    for i in range(iters):
        # menjamo resenje
        # promeni_resenje
        # ako je nedopustivo , vrati na prethodno i nastavi dalje
        success, old_coloring = change_coloring_vector(graph)
        if not success:
            graph.coloring_vector = old_coloring.copy()
            continue
        new_value = calc_solution_value(graph)
        if new_value < curr_value:
            curr_value = new_value
            if new_value < best_value:
                best_value = curr_value
        else:
            #sa nekom malom verovatnocom prihvatamo to gore resenje
            #sirimo prostor pretrage
            p = 1.0 / i**0.5
            q = random.uniform(0,1)
            if q < p:
                curr_value = new_value
            else:
            # nastavi sa starim resenjem
             graph.coloring_vector = old_coloring
    return best_value

if __name__=='__main__':
    # g = Graph(3)
    # g.add_edge(1,2)
    # g.add_edge(0,2)
    # g.add_edge(1,0)
    # print(g)
    #testiramo random funkciju
    # g.random_graph()
    # print(g)

    # print(g.coloring_vector)
    # print(calc_solution_value(g))
    # print(is_coloring_valid(g))

    #graf moj iz sveske
    g = Graph(6)
    g.add_edge(0,1)
    g.add_edge(0,5)
    g.add_edge(1,3)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(2,4)
    g.add_edge(4,5)
    assign_color(g)
    # print(calc_solution_value(g))
    print(g)
    print(local_search(g,10000))
    print(simulated_annealing(g,1000000))
    print(g.coloring_vector)