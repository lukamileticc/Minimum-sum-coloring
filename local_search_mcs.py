#!/usr/bin/python3

import numpy as np
class Graph():

    def __init__(self,num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.adjacency_list = np.array([[0 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)])

        #vector of color
        # self.coloring_vector = np.array([np.random.randint(0,self.num_of_vertices) for _ in range(self.num_of_vertices)])
        self.coloring_vector = np.array([i for i in range(num_of_vertices)])
    #neusmeren graf
    def add_edge(self, u, v):
        self.adjacency_list[u][v] = 1
        self.adjacency_list[v][u] = 1

    #ispis random grafa
    def random_graph(self):
        n = self.num_of_vertices
        self.adjacency_list = np.random.randint(0,2,(n,n))
        for i in range(n):
            for j in range(n):
                if self.adjacency_list[i][j] == 1:
                    self.adjacency_list[j][i] = 1
    def __str__(self):
       return str(self.adjacency_list)



def assign_color(graph):
    pass

# to check current coloring is valid or not
def is_coloring_valid(graph):
    for vertex,color in enumerate(graph.coloring_vector):
        for neighbor_vertex in graph.adjacency_list[vertex]:
            if color == graph.coloring_vector[neighbor_vertex] and graph.adjacency_list[vertex][neighbor_vertex] == 1:
                return False
    return True

# calculate the number of colors which is used
def loss_function(graph):
    return  len(set(graph.coloring_vector))



def simulated_annealing():
    pass

if __name__=='__main__':
    g = Graph(3)
    g.add_edge(1,2)
    g.add_edge(0,2)
    g.add_edge(1,0)
    # print(g)
    #testiramo random funkciju
    # g.random_graph()
    print(g)

    print(g.coloring_vector)
    print(loss_function(g))
    print(is_coloring_valid(g))