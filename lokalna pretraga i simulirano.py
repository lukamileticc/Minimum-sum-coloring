#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


def randomGraph( numvertices):
    n=numvertices
    adjacency_matrix = np.random.randint(0,2,(n,n))
    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] == 1:
                adjacency_matrix[j][i] =1
        adjacency_matrix[i][i]=0
            
        
    return  adjacency_matrix


# In[3]:


from copy import deepcopy 
from matplotlib import pyplot as plt

def local_search(graph, max_iters):
    solution = initialize(len(graph[0]))
    value = calc_solution_value(solution, graph)
    
    
    xs = []
    ys = []
    for i in range(max_iters):
        new_solution = make_small_change(solution)
        new_value = calc_solution_value(new_solution, graph)
        
        if new_value < value:
            value = new_value
            solution = deepcopy(new_solution)
            
            
        xs.append(i)
        ys.append(value)
        
    
    #iscrtavanje
    plt.plot(xs,ys,color='blue')
    plt.show()
    
    return solution, value


# In[5]:


local_search(randomGraph(30), 100)


# In[6]:


from copy import deepcopy 
from matplotlib import pyplot as plt

def simulated_annealing(graph, max_iters):
    solution = initialize(len(graph[0]))
    value = calc_solution_value(solution, graph)
    
    
    xs = []
    ys = []
    for i in range(1,max_iters):
        new_solution = make_small_change(solution)
        new_value = calc_solution_value(new_solution, graph)
        
        if new_value < value:
            value = new_value
            solution = deepcopy(new_solution)
            
        else:
            p = 1.0 //i**0.5
            q= random.uniform(0,1)
            if q < p:
                value = new_value
                solution = deepcopy(new_solution)
            

        xs.append(i)
        ys.append(value)
        
    
    #iscrtavanje
    plt.plot(xs,ys,color='blue')
    plt.show()
    
    return solution, value


# In[8]:


simulated_annealing(randomGraph(20) , 100)


# In[ ]:




