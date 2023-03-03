#!/usr/bin/env python
# coding: utf-8

# In[13]:


import random
import numpy as np
class Graph():
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
  
    # A utility function to check
    # if the current color assignment
    # is safe for vertex v
    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True
  
    # A recursive utility function to solve m
    # coloring  problem
    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True
  
        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0
  
    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == None:
            return False
  
        # Print the solution
        print("Solution exist and Following are the assigned colours:")
        for c in colour:
            print(c, end=' ')
            
        
        print("number of color is")
        print(max(colour))
        return True
    
    
    
    def randomGraph(self, numvertices):
        n=numvertices
        adjacency_matrix = np.random.randint(0,2,(n,n))
        for i in range(n):
            for j in range(n):
                if adjacency_matrix[i][j] == 1:
                    adjacency_matrix[j][i] =1
            adjacency_matrix[i][i]=0
            
        print(adjacency_matrix)
        return  adjacency_matrix
        
        
  
  
# Driver Code
if __name__ == '__main__':

    numvertices= random.randrange(3,100)
    g = Graph(numvertices)
    #g= Graph(5)
    print("number of enges")
    print(numvertices)
    g.graph = g.randomGraph(numvertices)
    
    if g.graphColouring(numvertices) == False:
        print("solution not exist")
    
    
   
    
  
  


# In[ ]:





# In[37]:





# In[48]:





# In[ ]:




