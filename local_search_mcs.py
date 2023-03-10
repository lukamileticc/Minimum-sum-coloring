#!/usr/bin/python3
import random
import numpy as np
from matplotlib import pyplot as plt
class Graph():

    def __init__(self,num_of_vertices=10):
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

                #na dijagonali ne zelimo jedinice
                if i == j:
                    self.adjacency_matrix[i][j]=0
    def __str__(self):
       return 'Num of vertices: \n' + str(self.num_of_vertices) + '\n' + "Adjacency_matrix: \n" + str(self.adjacency_matrix)

    def load_graph_from_file(self,filename):
        self.adjacency_matrix = np.ndarray([])
        with open(filename,"r") as f:
            self.num_of_vertices = int(f.readline())
            self.adjacency_matrix = np.loadtxt(f)


    def save_graph_to_file(self,filename):
        with open(filename, "w") as f:
            f.write(str(g.num_of_vertices))
            f.write('\n')
            np.savetxt(f, self.adjacency_matrix, fmt='%d')


def assign_color(graph):
    # vector of color
    #random bojenje--- ipak NE MOZE RANDOM JER SKORO NIKAD NECE BITI VALIDNO
    graph.coloring_vector = np.array([np.random.randint(0,graph.num_of_vertices) for _ in range(graph.num_of_vertices)])
    # razlicito bojenje(svi cvorovi napocetku razliciti) - ovo je UVEK VALIDNO
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


#OVO JE PROBLEMATICNA FUNKCIJA -- NE ZNAM KAKO DA NADJEM SUSEDNO RESENJE, TJ 'SUSEDNO BOJENJE'
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
    print(best_value)

    #za iscrtavanje grafika
    xs = []
    ys = []

    for i in range(1,iters):
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

        xs.append(i)
        ys.append(new_value)

    # print(xs)
    # print(ys)

    #iscrtavnanje grafika
    plt.title('Solution value through the iterations: ')
    plt.xlabel('Iters')
    plt.ylabel('Target function')
    plt.plot(xs,ys,color='blue')
    plt.show()

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
    # g = Graph(6)
    # g.add_edge(0,1)
    # g.add_edge(0,5)
    # g.add_edge(1,3)
    # g.add_edge(1,2)
    # g.add_edge(2,3)
    # g.add_edge(2,4)
    # g.add_edge(4,5)
    # assign_color(g)
    # # print(calc_solution_value(g))
    # print(g)
    # print(local_search(g,10000))
    # print(simulated_annealing(g,1000000))
    # print(g.coloring_vector)

#i kod uporedjivanja moramo postaviti isti seed
#isprobati i na seven bridges-u(platformi - izabrati neki jaki komp)

    g = Graph(30)
    g.random_graph()
    # g.save_graph_to_file("random_graph.txt")
    g.load_graph_from_file("random_graph.txt")
    print(g)



    random.seed(11231432)
    print(simulated_annealing(g,10000))