import random
import numpy as np
class Graph():
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
  
    #proveravamo da li mozemo na taj nacin da obojimo graf
    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True
  
    #proveravamo da li mozemo sa m boja da obojimo graf
    
    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True
        #krecemo od broja 1 i nastavljamo sa prvom slobodnom bojom sa kojom moze da se oboji
        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                #kada obojimo taj cvor pozivamo rekurzivno za naredni
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0
  
    #bojimo graf
    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == None:
            return False, 0,colour
  
       
        return True , max(colour),colour
    
    #numerisemo random graf
    
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

    numvertices= random.randrange(3,15)
    g = Graph(numvertices)
    #g= Graph(5)
    minsuma = 9999999999999
    
    suma =0
    print("number of enges")
    print(numvertices)
    g.graph = g.randomGraph(numvertices)
    true, num, colour =g.graphColouring(numvertices)
    for c in colour:
        suma= suma +c
    
    if suma <minsuma:
        minsuma = suma
        
        
    print('prva suma koju nadje  je: ',minsuma)
    if true == False:
        print("solution not exist")
    
    elif true == True:
        for i in range(num-1):
            suma =0
            stop, newnum, colour1 =g.graphColouring(num-i-1)
            
            if stop == True:
                for c in colour1:
                    suma= suma +c
                
                if suma <minsuma:
                    minsuma = suma
                colour=colour1
                continue
            elif stop == False:
                print("Solution exist and Following are the assigned colours:")
                for c in colour:
                    print(c,end=' ')
                print()
                print('minimumna suma je: ' , minsuma)
                print('min num of colour are ',max(colour))
                break
   
  
    



