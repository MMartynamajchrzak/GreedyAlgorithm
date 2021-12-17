import random

from GeneticAlgorithm import GeneticAlgorithm, read


def main():
    files_to_test = ['files/ali535.tsp', 'files/berlin11_modified.tsp', 'files/berlin52.tsp',
                     'files/fl417.tsp', 'files/kroA100.tsp', 'files/kroA150.tsp',
                     'files/kroA200.tsp', 'files/nrw1379.tsp', 'files/pr2392.tsp']

    # choose one of the files from above
    file_name = files_to_test[1]

    # read file
    file = read(file_name)

    # get list of cities (by indexes) with the shortest path starting from one random city
    cities = GeneticAlgorithm.greedy_algorithm(file)

    # create an initial population of length 100
    initial_pop = GeneticAlgorithm.population(cities=cities, coords=file)

    # find the best solution of the population
    best_solution = GeneticAlgorithm.fitness(initial_pop, file)

    # for now while till 50 generations
    gen = 0
    current_pop = []
    all_generations = [initial_pop]
    path_with_distance = []

    while gen < 50:
        print(f"GENERATION #{gen}")

        # change here initial pop to pop(t-1)
        while len(current_pop) != len(initial_pop):

            parent1 = GeneticAlgorithm.tournament(initial_pop, file)
            parent2 = GeneticAlgorithm.tournament(initial_pop, file)

            # probability for a crossover is 50%
            if random.randint(0, 100) < 50:
                cross = GeneticAlgorithm.crossover(parent1, parent2)
                solution = cross.copy()
            else:
                solution = parent1.copy()

            # probability for a mutation is 5%
            if random.randint(0, 100) > 95:
                current_solution = GeneticAlgorithm.inversion(solution)
                distance = GeneticAlgorithm.distance(current_solution, file)
                current_pop.append(current_solution)

                # just to keep track of path with distance
                path_with_distance.append((current_solution, distance))

            # no mutation, result from crossover/parent
            else:
                current_solution = solution.copy()
                distance = GeneticAlgorithm.distance(current_solution, file)
                current_pop.append(current_solution)

                # just to keep track of path with distance
                path_with_distance.append((current_solution, distance))

            # check if the best solution from initial population is better than current solution
            # if so new best solution is current solution
            if GeneticAlgorithm.distance(best_solution, file) > distance:
                best_solution = current_solution

        print(f"Current pop is {current_pop}")
        gen += 1
        all_generations.append(current_pop)
        initial_pop = all_generations[-1]
        current_pop = []

    print(f"The best solution and its distance is {best_solution} {GeneticAlgorithm.distance(best_solution, file)}")
    return best_solution


if __name__ == "__main__":
    main()
