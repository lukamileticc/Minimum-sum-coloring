#!/usr/bin/env python
# coding: utf-8




import random
import numpy as np
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

def  calc_solution_value(solution, graph):
    n= len(graph[0])
    
    
    x_boje= [0 for _ in range(n)]
    zauzete= [[]  for _ in range(n)]
            
    for i in range(len(solution)):
        ind = solution.index(i)
       
        if i == 0:

            x_boje[ind] = 1
            for j in range(n):
                if graph[ind][j] == 1:
                    zauzete[j].append(1)

        else:
            slobodne = []
            for z in range(1,n+1):
                if z not in zauzete[ind]:
                    slobodne.append(z)
                    x_boje[ind] = min(slobodne)
                    for j in range(n):
                        if graph[ind][j] == 1:
                            zauzete[j].append(x_boje[ind])



            #ovde sad treba da saberemo
    #print(x_boje)       
    #print(sum(x_boje))
    return sum(x_boje) 



def randomGraph( numvertices):
    n=numvertices
    adjacency_matrix = np.random.randint(0,2,(n,n))
    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] == 1:
                adjacency_matrix[j][i] =1
        adjacency_matrix[i][i]=0
            
        
    return  adjacency_matrix





from copy import deepcopy 
from matplotlib import pyplot as plt
import random




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
    n= len(graph[0])
    solution = initialize(n)
    value = calc_solution_value(solution, graph)
    xs = []
    ys = []
    for i in range(max_iters):
        for k in range(1, k_max):
            new_solution = shaking(solution, k)
#             new_solution = LS(new_solution)
            new_value = calc_solution_value(new_solution, graph)
            
            if new_value < value or (new_value == value and random.random() < move_prob):
                value = new_value
                solution = deepcopy(new_solution)
                break
        xs.append(i)
        ys.append(value)
        
    #iscrtavanje
    plt.plot(xs,ys,color='blue')
    plt.show()
    
    return solution, value





