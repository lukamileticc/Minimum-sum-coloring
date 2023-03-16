from graph import Graph
from collections import Counter

# proveravamo da li mozemo na taj nacin da obojimo graf
def isSafe(graph, v, colors_vector, c):
    for i in range(graph.num_of_vertices):
        if graph.adjacency_matrix[v][i] == 1 and colors_vector[i] == c:
            return False
    return True

# proveravamo da li mozemo sa m boja da obojimo graf
def graph_coloring_util(graph, m, colors_vector, v):
    if v == graph.num_of_vertices:
        return True
    # krecemo od broja 1 i nastavljamo sa prvom slobodnom bojom sa kojom moze da se oboji
    for c in range(1, m + 1):
        if isSafe(graph, v, colors_vector, c) == True:
            colors_vector[v] = c
            # kada obojimo taj cvor pozivamo rekurzivno za naredni
            if graph_coloring_util(graph, m, colors_vector, v + 1) == True:
                return True
            colors_vector[v] = 0

# pokusavamo da obojimo graf sa m boja
def graph_coloring(graph,m):
    colors_vector = [0 for _ in range(graph.num_of_vertices)]
    if graph_coloring_util(graph, m, colors_vector, 0) == None:
        return False, 0, colors_vector
    return True, max(colors_vector), colors_vector

#stari calc_solution trebace
def minimum_color_sum(colors_vector):

    #[1,2,4,7,1,3,6,7,7,2,4] boje svakog cvora
    #[(1,2),(2,2),(3,1),(4,2),(6,1),(7,3)] broj pojavljivanja svake boje
    #[(7,3),(4,2),(2,2),(1,2),(6,1),(3,1)] sortiramo po boju pojavljivanja tj.drugom parametru
    # 3*1 + 2*2 + 2*3 + 2*4 + 1*5 + 1*6  funkcija cilja=suma(broj_pojavljuvanja*indeks_unizu)

    tmp = list(map(lambda el: (el,1),colors_vector))
    tmp = list(set([(el[0], Counter(tmp)[el]) for el in tmp]))
    tmp = sorted(tmp, key = lambda el: el[1],reverse=True)

    total_sum = 0
    for index,tupp in enumerate(tmp):
        total_sum += (index+1)*tupp[1]

    return total_sum


def brute_force(graph):
    num_of_color = 0
    #pokusavamo da obojimo graf sa minimalnim brojem boja
    for i in range(2,graph.num_of_vertices + 1):
        success, num_of_color, colors_vector = graph_coloring(graph,i)
        # ako je graf uspesno obojen
        if success == True:
            print("Graf je obojen sa minimalno " + str(num_of_color) + " boja")
            print(colors_vector)
            sum = minimum_color_sum(colors_vector)
            print("Minimalna suma: ", sum)
            break

if __name__ == '__main__':
    g = Graph(16)
    g.random_graph()
    g.save_graph_to_file("small_random_graph.txt")
    # g.load_graph_from_file("small_random_graph.txt")
    print(g)

    # brute_force(g)



    # staro --vrtno nece TREBATI
    # numvertices= random.randrange(3,15)
    # g = Graph(numvertices)
    # #g= Graph(5)
    # minsuma = 9999999999999
    #
    # suma =0
    # print("number of enges")
    # print(numvertices)
    # g.graph = g.randomGraph(numvertices)
    # true, num, colors_vector =g.graphcolors_vectoring(numvertices)
    # for c in colors_vector:
    #     suma= suma +c
    #
    # if suma <minsuma:
    #     minsuma = suma
    #
    #
    # print('prva suma koju nadje  je: ',minsuma)
    # if true == False:
    #     print("solution not exist")
    #
    # elif true == True:
    #     for i in range(num-1):
    #         suma =0
    #         stop, newnum, colors_vector1 =g.graphcolors_vectoring(num-i-1)
    #
    #         if stop == True:
    #             for c in colors_vector1:
    #                 suma= suma +c
    #
    #             if suma <minsuma:
    #                 minsuma = suma
    #             colors_vector=colors_vector1
    #             continue
    #         elif stop == False:
    #             print("Solution exist and Following are the assigned colors_vectors:")
    #             for c in colors_vector:
    #                 print(c,end=' ')
    #             print()
    #             print('minimumna suma je: ' , minsuma)
    #             print('min num of colors_vector are ',max(colors_vector))
    #             break
   




