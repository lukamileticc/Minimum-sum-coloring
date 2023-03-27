import random
import numpy as np
import time
from matplotlib import pyplot as plt

from VNS import vns
from graph import Graph
from genetic_algorithm_msc import ga
from local_search_mcs import local_search
from simulated_annealing_msc import simulated_annealing
from hybrid_ga_sa import hybrid

def draw_graph(title,path_to_save, xs, ys):
    # iscrtavnanje grafika
    font1 = {'family': 'fantasy', 'color': 'black', 'size': 10}
    plt.title(title,fontdict=font1)
    plt.xlabel('Iters')
    plt.ylabel('Value')
    plt.plot(xs, ys, color='blue')
    fig = plt.gcf()
    plt.show()
    plt.draw()
    fig.savefig(path_to_save,dpi=100)

if __name__ == '__main__':
    g = Graph()
    file = 'miles1500.txt'
    g.load_dimacs_file('graph_instances/group_2/' + file)
    # print(g)
    iteration_number = 5
    best_value = float('inf')
    avg_value = 0

    max_iters = 10000

    # parametri genetskog algoritma
    POPULATION_SIZE = 100
    NUM_OF_GENERATIONS = 100
    ELITISM_SIZE = POPULATION_SIZE // 5
    TOURNAMENT_SIZE = 10
    MUTATION_PROB = 0.05  # 5%

    #parametri vns-a
    k_max = 3
    move_prob = 0.5

    random.seed(32452)
    np.random.seed(32452)

    xs = []
    ys = []
    start = time.time()
    for i in range(iteration_number):
        print(i)
        _, curr_value = vns(g,max_iters,k_max,move_prob)
        xs.append(i)
        ys.append(curr_value)
        avg_value += curr_value
        if curr_value < best_value:
            best_value = curr_value
    end = time.time()

    title = "VNS(k_max=3, iters=10000),\nGraph instance:" + file + '(128 10396),\nTime:' + str(
        round(end - start, 3)) + ' sec, Avg value:' + str(avg_value/iteration_number) + ' Best value:' + str(best_value)
    draw_graph(title, 'graphic_results/' + title + '.png', xs, ys)

    best_value = float('inf')
    avg_value = 0

    xs = []
    ys = []
    k_max = 5
    start = time.time()
    for i in range(iteration_number):
        print(i)
        _, curr_value = vns(g, max_iters,k_max,move_prob)
        xs.append(i)
        ys.append(curr_value)
        avg_value += curr_value
        if curr_value < best_value:
            best_value = curr_value
    end = time.time()

    title = "VNS(k_max=5, iters=10000),\nGraph instance:" + file + '(128 10396),\nTime:' + str(
        round(end - start, 3)) + ' sec, Avg value:' + str(avg_value / iteration_number) + ' Best value:' + str(
        best_value)
    draw_graph(title, 'graphic_results/' + title + '.png', xs, ys)


    best_value = float('inf')
    avg_value = 0

    xs = []
    ys = []
    start = time.time()
    for i in range(iteration_number):
        print(i)
        _, curr_value = local_search(g,max_iters)
        xs.append(i)
        ys.append(curr_value)
        avg_value += curr_value
        if curr_value < best_value:
            best_value = curr_value
    end = time.time()

    title = "Local search(iters=10000),\nGraph instance:" + file + '(128 10396),\nTime:' + str(
        round(end - start, 3)) + ' sec, Avg value:' + str(avg_value/iteration_number) + ' Best value:' + str(best_value)
    draw_graph(title, 'graphic_results/' + title + '.png', xs, ys)


    best_value = float('inf')
    avg_value = 0

    xs = []
    ys = []
    start = time.time()
    for i in range(iteration_number):
        print(i)
        _, curr_value = simulated_annealing(g,max_iters)
        xs.append(i)
        ys.append(curr_value)
        avg_value += curr_value
        if curr_value < best_value:
            best_value = curr_value
    end = time.time()

    title = "Simulated annealing(iters=10000),\nGraph instance:" + file + '(128 10396),\nTime:' + str(
        round(end - start, 3)) + ' sec, Avg value:' + str(avg_value/iteration_number) + ' Best value:' + str(best_value)
    draw_graph(title, 'graphic_results/' + title + '.png', xs, ys)

    best_value = float('inf')
    avg_value = 0

    xs = []
    ys = []
    start = time.time()
    for i in range(iteration_number):
        print(i)
        _, curr_value = ga(g,POPULATION_SIZE,NUM_OF_GENERATIONS,ELITISM_SIZE,TOURNAMENT_SIZE,MUTATION_PROB)
        xs.append(i)
        ys.append(curr_value)
        avg_value += curr_value
        if curr_value < best_value:
            best_value = curr_value
    end = time.time()

    title = "Genetic algorithm(roulette selection),\nGraph instance:" + file + '(128 10396),\nTime:' + str(
        round(end - start, 3)) + ' sec, Avg value:' + str(avg_value / iteration_number) + ' Best value:' + str(
        best_value)
    draw_graph(title, 'graphic_results/' + title + '.png', xs, ys)

    best_value = float('inf')
    avg_value = 0

    xs = []
    ys = []
    start = time.time()
    for i in range(iteration_number):
        print(i)
        _, curr_value = hybrid(g, POPULATION_SIZE, NUM_OF_GENERATIONS, ELITISM_SIZE, TOURNAMENT_SIZE, MUTATION_PROB)
        xs.append(i)
        ys.append(curr_value)
        avg_value += curr_value
        if curr_value < best_value:
            best_value = curr_value
    end = time.time()

    title = "Hybrid(ga(roulette) + sa(iters=100)),\nGraph instance:" + file + '(128 10396),\nTime:' + str(
        round(end - start, 3)) + ' sec, Avg value:' + str(avg_value / iteration_number) + ' Best value:' + str(
        best_value)
    draw_graph(title, 'graphic_results/' + title + '.png', xs, ys)
