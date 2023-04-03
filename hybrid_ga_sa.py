from copy import deepcopy
import random
import simulated_annealing_msc
from simulated_annealing_msc import calc_solution_value
from genetic_algorithm_msc import Individual, roulette_selection, crossover, mutation_better, tournament_selection
from graph import Graph
from matplotlib import pyplot as plt

def draw_graph(xs, ys):
    # iscrtavnanje grafika
    plt.title('Hybrid(ga + sa): Solution value through the iterations: ')
    plt.xlabel('Iters')
    plt.ylabel('Target function')
    plt.plot(xs, ys, color='blue')
    plt.show()
def simulated_annealing(graph,init_solution, max_iters):
    #initialize solution
    # solution = initialize(graph.num_of_vertices)
    solution = init_solution
    curr_value,_ = calc_solution_value(solution, graph)

    best_solution = deepcopy(solution)
    best_value = curr_value

    # za iscrtavanje grafika
    # xs = []
    # ys = []

    for i in range(1,max_iters+1):
        #malo promenimo resenje
        new_solution = simulated_annealing_msc.make_small_change(solution)
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

        # xs.append(i)
        # ys.append(curr_value)

    # draw_graph(xs,ys)

    return best_solution,best_value


def hybrid(graph,POPULATION_SIZE, NUM_OF_GENERATIONS, ELITISM_SIZE,TOURNAMENT_SIZE,MUTATION_PROB):
    # pravim populaciju
    population = [Individual(graph) for _ in range(POPULATION_SIZE)]
    new_population = [Individual(graph) for _ in range(POPULATION_SIZE)]

    #za crtanje
    xs = []
    ys = []

    for i in range(NUM_OF_GENERATIONS):
        # izdavajamo najbolje-moramo sortirati
        population.sort(key=lambda x: x.fitness, reverse=True)
        # kopiramo najbolje
        new_population[:ELITISM_SIZE] = population[:ELITISM_SIZE]

        # ostale jedinke ukrstamo
        for j in range(ELITISM_SIZE, POPULATION_SIZE, 2):
            # parent1 = tournament_selection(population,TOURNAMENT_SIZE,graph)
            # parent2 = tournament_selection(population,TOURNAMENT_SIZE,graph,forbiden = parent1)

            parent1 = roulette_selection(population)
            parent2 = roulette_selection(population)

            # choices = {chromosome: chromosome.fitness for chromosome in population}

            crossover(parent1,
                      parent2,
                      new_population[j],
                      new_population[j + 1])
            mut_allowed = random.uniform(0,1)
            if mut_allowed < MUTATION_PROB:
                # mutation(new_population[j], MUTATION_PROB)
                # mutation(new_population[j + 1], MUTATION_PROB)
                mutation_better(new_population[j])
                mutation_better(new_population[j + 1])

            new_population[j].fitness = new_population[j].calc_fitness(graph)
            new_population[j + 1].fitness = new_population[j + 1].calc_fitness(graph)
        # HYBRID
        # poboljsavamo malo najbolju jedinku
        sol,val = simulated_annealing(graph,deepcopy(new_population[0].code), max_iters=100)
        new_population[0].code = sol
        new_population[0].fitness = 1.0/val

        xs.append(i)
        ys.append(1.0 / max(population).fitness)

        population = new_population
    #iscrtavanje grafika
    draw_graph(xs,ys)
    best_individual = max(population)
    # print(best_individual.code)
    # print(best_individual.fitness)
    # print(1.0 / best_individual.fitness)

    return best_individual.code , 1.0 / best_individual.fitness

if __name__ == '__main__':
    # parametri genetskog algoritma
    POPULATION_SIZE = 100
    NUM_OF_GENERATIONS = 100
    ELITISM_SIZE = POPULATION_SIZE // 5
    TOURNAMENT_SIZE = 10
    MUTATION_PROB = 0.05  # 5%

    # #pravimo graf
    g = Graph(12)
    g.random_graph()
    # g.save_graph_to_file("our_graph_instances/random_graph.txt")
    g.load_graph_from_file("our_graph_instances/small_random_graph.txt")
    # # print(g)

    solution, curr_value = hybrid(g,POPULATION_SIZE,NUM_OF_GENERATIONS,ELITISM_SIZE,TOURNAMENT_SIZE,MUTATION_PROB)
    print("#########")
    print(solution)
    print(curr_value)
    suma,_ = calc_solution_value(solution,g)
    print(suma)