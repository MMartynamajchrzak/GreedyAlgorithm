from GeneticAlgorithm import GeneticAlgorithm, PART_OF_POP_FOR_TOURNAMENT, read


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
    city_2 = GeneticAlgorithm.greedy_algorithm(file)

    # create an initial population of length 100
    pop = GeneticAlgorithm.population(cities=cities, coords=file)

    # find the best n% of the population
    GeneticAlgorithm.fitness(pop, file)

    # make mutations and inversions
    GeneticAlgorithm.mutations(cities, file)
    GeneticAlgorithm.inversion(cities, file)

    # tournament
    GeneticAlgorithm.tournament(PART_OF_POP_FOR_TOURNAMENT, pop, file)

    # croosover of two parents
    GeneticAlgorithm.croosover(cities, city_2)


if __name__ == "__main__":
    main()
