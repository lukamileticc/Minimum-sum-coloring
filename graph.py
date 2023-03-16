import numpy as np
class Graph():

    def __init__(self,num_of_vertices=10):
        self.num_of_vertices = num_of_vertices
        self.adjacency_matrix = np.array([[0 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)])

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

                #na dijagonali ne zelimo jedinice
                if i == j:
                    self.adjacency_matrix[i][j]=0

    def get_edges(self,i,j):
        return self.adjacency_matrix[i][j]
    def __str__(self):
       return 'Num of vertices: \n' + str(self.num_of_vertices) + '\n' + "Adjacency_matrix: \n" + str(self.adjacency_matrix)

    def load_graph_from_file(self,filename):
        self.adjacency_matrix = np.ndarray([])
        with open(filename,"r") as f:
            self.num_of_vertices = int(f.readline())
            self.adjacency_matrix = np.loadtxt(f)


    def save_graph_to_file(self,filename):
        with open(filename, "w") as f:
            f.write(str(self.num_of_vertices))
            f.write('\n')
            np.savetxt(f, self.adjacency_matrix, fmt='%d')
