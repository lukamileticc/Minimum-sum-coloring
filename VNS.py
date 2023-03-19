#!/usr/bin/env python
# coding: utf-8
import random
import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt
from graph import Graph

def initialize(num_resources):
    #generisemo varijacije
    solution = list(np.random.permutation(num_resources))
    return solution
def make_small_change(solution):
    poz1 = random.randrange(0, len(solution))
    poz2= random.randrange(0, len(solution))
    pom = solution[poz1]
    solution[poz1]= solution[poz2]
    solution[poz2] = pom
    
    return solution

def draw_graph(xs, ys):
    # iscrtavnanje grafika
    plt.title('Variable Neighborhood Search (VNS): Solution value through the iterations: ')
    plt.xlabel('Iters')
    plt.ylabel('Target function')
    plt.plot(xs, ys, color='blue')
    plt.show()
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

def shaking(solution, k):
   
    #treba da na slucajan nacin izaberemo k pozicija
    n= len(solution)
    poz= random.sample(range(1, n), k)
    poz.sort()
    
    
    #ovde treba da izvrsimo shaking
    for i in poz:
        if i == poz[0]:
            #ovde se radi o prvom izmestanju
            list1=solution[0:i]
            list1.reverse()
            solution[0:i] = list1
            #print(solution)
        else:
            #indeks pozicije
            p = poz.index(i)
            list1 = solution[poz[p-1]:i]
            list1.reverse()
            solution[poz[p-1]:i] = list1
            #print(solution)
            
            
    #ovde vrsimo obrtanje do kraja:
    p= poz[k-1]
    list1= solution[p:n]
    list1.reverse()
    #print(list1)
    solution[p:n]=list1
    #print(solution)

    return solution

def vns(graph, max_iters, k_max, move_prob):
    n= graph.num_of_vertices
    solution = initialize(n)
    value,_ = calc_solution_value(solution, graph)
    xs = []
    ys = []
    for i in range(max_iters):
        for k in range(1, k_max):
            new_solution = shaking(deepcopy(solution), k)
#             new_solution = LS(new_solution)
            new_value,_ = calc_solution_value(new_solution, graph)
            
            if new_value < value or (new_value == value and random.random() < move_prob):
                value = new_value
                solution = deepcopy(new_solution)
                # print(solution)
                break
        xs.append(i)
        ys.append(value)
        
    #iscrtavanje
    draw_graph(xs,ys)
    
    return solution, value

if __name__ == '__main__':
    g = Graph(50)
    g.random_graph()
    g.save_graph_to_file("random_graph.txt")
    g.load_graph_from_file("random_graph.txt")
    # print(g)

    max_iters = 10000
    k_max = 3
    move_prob = 0.5
    solution, curr_value = vns(g,max_iters,k_max,move_prob)
    print("#########")
    print(solution)
    print(curr_value)
    suma,_ = calc_solution_value(solution,g)
    print(suma)