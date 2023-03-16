#!/usr/bin/python3
import random
import numpy as np

from copy import deepcopy
from matplotlib import pyplot as plt
from graph import Graph

def free_colors(zauzete, ind, n):
    slobodne = []
    for i in range(1,n+1):
        if i not in zauzete[ind]:
            slobodne.append(i)
    return slobodne

def calc_solution_value(solution, graph):
    n = graph.num_of_vertices
    x_boje = [0 for _ in range(n)]
    zauzete = [[] for _ in range(n)]

    for i in range(len(solution)):
        ind = solution.index(i)
        if i == 0:
            x_boje[ind] = 1
            for j in range(n):
                if graph.get_edges(ind,j) == 1:
                    zauzete[j].append(1)
        else:
            slobodne = free_colors(zauzete,ind,n)
            x_boje[ind] = min(slobodne)
            for j in range(n):
                if graph.get_edges(ind,j) == 1:
                    zauzete[j].append(x_boje[ind])

    # print(x_boje)
    # print(sum(x_boje))
    return sum(x_boje), x_boje

def initialize(num_resources):
    #generisemo permutacije
    solution = list(np.random.permutation(num_resources))
    return solution

def make_small_change(solution):
    poz1 = random.randrange(0, len(solution))
    poz2 = random.randrange(0, len(solution))
    pom = solution[poz1]
    solution[poz1] = solution[poz2]
    solution[poz2] = pom

    return solution
def draw_graph(xs, ys):
    # iscrtavnanje grafika
    plt.title('Solution value through the iterations: ')
    plt.xlabel('Iters')
    plt.ylabel('Target function')
    plt.plot(xs, ys, color='blue')
    plt.show()

def simulated_annealing(graph, max_iters):
    #initialize solution
    solution = initialize(graph.num_of_vertices)
    curr_value,_ = calc_solution_value(solution, graph)

    best_solution = deepcopy(solution)
    best_value = curr_value

    # za iscrtavanje grafika
    xs = []
    ys = []

    for i in range(1,max_iters+1):
        #malo promenimo resenje
        new_solution = make_small_change(solution)
        new_value,_ = calc_solution_value(new_solution,graph)
        if new_value < curr_value:
            solution = deepcopy(new_solution)
            curr_value = new_value
            if new_value < best_value:
                best_value = new_value
                best_solution = deepcopy(new_solution)
        else:
            #ponekad prihvati i to losije resenje
            p = 1.0 // i**0.5
            q = random.uniform(0,1)
            if q < p:
                curr_value = new_value
                solution = deepcopy(new_solution)

        xs.append(i)
        ys.append(curr_value)

    draw_graph(xs,ys)

    return best_solution,best_value

if __name__=='__main__':

    g = Graph(30)
    g.random_graph()
    # g.save_graph_to_file("random_graph.txt")
    g.load_graph_from_file("random_graph.txt")
    # print(g)

    solution, curr_value = simulated_annealing(g, 10000)
    print(solution)
    print(curr_value)
    suma, _ = calc_solution_value(solution, g)
    print(suma)