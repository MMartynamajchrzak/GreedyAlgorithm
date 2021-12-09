import random
from math import sqrt


def read(file_name):
    with open(file_name) as file:
        coord = [tuple(i.split()[0:3]) for i in file.readlines()[6:]]

    return coord


def greedy_algorithm(coord):
    final_distance = 0

    # choosing one random element from which to start
    r = random.randint(1, len(coord))
    new_coord = [r]

    # list of numbers representing indexes from remaining cities
    remaining_cities = [i for i in range(1, len(coord)+1) if i not in new_coord]

    while len(remaining_cities) > 0:
        # while there are still cities not taken into account
        r = new_coord[-1]
        minimum = -1
        closest = 0

        for idx, item in enumerate(coord):
            # loop through each item in order to get the smallest distance for a current point
            if item[0] is not new_coord[-1] and idx + 1 not in new_coord:
                dist = sqrt((float(coord[r-1][1]) - float(item[1]))**2 + (float(coord[r-1][2]) - float(item[2]))**2)

                # finding closest city
                if minimum == -1 or dist < minimum:
                    minimum = dist
                    closest = int(item[0])

        final_distance += minimum
        new_coord.append(closest)
        remaining_cities.remove(closest)

    result = f"list of indexes of cities sorted by the closest distance {new_coord} " \
             f"\nGive the total distance of {format(final_distance, '.2f')}"

    return new_coord


# Distance
def distance(cities, coord):
    path = 0

    for idx, item in enumerate(cities):
        # case we return from last to first city
        if idx == len(cities) - 1:

            dist = sqrt((float(coord[cities[idx] - 1][1]) - float(coord[cities[0] - 1][1])) ** 2 +
                        (float(coord[cities[idx] - 1][2]) - float(coord[cities[0] - 1][2])) ** 2)
            path += dist
        else:
            dist = sqrt((float(coord[cities[idx+1]-1][1]) - float(coord[cities[idx]-1][1])) ** 2 +
                        (float(coord[cities[idx+1]-1][2]) - float(coord[cities[idx]-1][2])) ** 2)
            path += dist

    return format(path, ".2f")


# Initial population
def population(cities, coords):
    pop = []
    for _ in range(89):
        random.shuffle(cities)
        new = list(cities)
        pop.append(new)

    for _ in range(11):
        greedy_results = greedy_algorithm(coords)
        pop.append(greedy_results)

    return pop


# Fitness function
def fitness(whole_population, coord):
    results = []
    for idx, item in enumerate(whole_population):
        dist = float(distance(whole_population[idx], coord))
        results.append([dist, item])

    fittest = sorted(results)[:50]

    print(f"50 results with the shortest path: {fittest}")

    return fittest


# Mutations for the population
def mutations(pop, coord):
    print(f"Population before mutations {pop} has distance: {distance(pop, coord)}")
    random_index = random.randint(0, len(pop)-1)
    random_index_2 = random.randint(0, len(pop)-1)

    pop[random_index], pop[random_index_2] = pop[random_index_2], pop[random_index]

    print(f"Population after mutations {pop} has distance: {distance(pop, coord)}")

    return pop


def inversion(pop, coord):
    random_index = random.randint(0, len(pop) - 1)
    random_index_2 = random.randint(0, len(pop) - 1)

    if random_index < random_index_2:
        smaller, bigger = random_index, random_index_2
    else:
        smaller, bigger = random_index_2, random_index

    print(f"Population before inversion {pop} has distance: {distance(pop, coord)}")

    to_reverse = pop[smaller:bigger]
    to_reverse.reverse()
    new_pop = pop
    del new_pop[smaller:bigger]
    new_pop[smaller:smaller] = to_reverse

    print(f"New population {new_pop} has distance: {distance(new_pop, coord)}")

    return new_pop


def main():
    file_name = 'files/berlin11_modified.tsp'

    # read file
    file = read(file_name)

    # get list of cities (by indexes) with the shortest path starting from one random city
    cities = greedy_algorithm(file)

    # create an initial population of length 100
    pop = population(cities=cities, coords=file)

    # find the best 50% of the population
    fitness(pop, file)

    # make mutations and inversions
    mutations(cities, file)
    inversion(cities, file)


if __name__ == "__main__":
    main()

# FILES to test

# greedy_algorithm('files/ali535.tsp')
# greedy_algorithm('files/berlin11_modified.tsp')
# greedy_algorithm('files/berlin52.tsp')
# greedy_algorithm('files/fl417.tsp')
# greedy_algorithm('files/kroA100.tsp')
# greedy_algorithm('files/kroA150.tsp')
# greedy_algorithm('files/kroA200.tsp')
# greedy_algorithm('files/nrw1379.tsp')
# greedy_algorithm('files/pr2392.tsp')
