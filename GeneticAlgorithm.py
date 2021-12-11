import random
from math import sqrt


PART_OF_POP_FOR_TOURNAMENT = 20


# parse
def read(file_name):
    with open(file_name) as file:
        coord = [tuple(i.split()[0:3]) for i in file.readlines()[6:]]

    return coord


# to flatten internal lists from two-dimensional list
def flatten(list_to_flatten):
    for sublist in list_to_flatten:
        if isinstance(sublist, list):
            for item in sublist:
                yield item
        else:
            yield sublist


def get_two_random_items(list_to_loop_through):
    random_index = random.randint(0, len(list_to_loop_through) - 1)
    random_index_2 = random.randint(0, len(list_to_loop_through) - 1)

    if random_index < random_index_2:
        smaller, bigger = random_index, random_index_2
    elif random_index == random_index_2:
        if random_index != len(list_to_loop_through) - 1:
            smaller, bigger = random_index, random_index_2 + 1
        else:
            smaller, bigger = random_index - 1, random_index_2
    else:
        smaller, bigger = random_index_2, random_index

    return smaller, bigger


class GeneticAlgorithm:

    @staticmethod
    def greedy_algorithm(coord):
        final_distance = 0

        # choosing one random element from which to start
        r = random.randint(1, len(coord))
        new_coord = [r]

        # list of numbers representing indexes from remaining cities
        remaining_cities = [i for i in range(1, len(coord) + 1) if i not in new_coord]

        while len(remaining_cities) > 0:
            # while there are still cities not taken into account
            r = new_coord[-1]
            minimum = -1
            closest = 0

            for idx, item in enumerate(coord):
                # loop through each item in order to get the smallest distance for a current point
                if item[0] is not new_coord[-1] and idx + 1 not in new_coord:
                    dist = sqrt(
                        (float(coord[r - 1][1]) - float(item[1])) ** 2 + (float(coord[r - 1][2]) - float(item[2])) ** 2)

                    # finding closest city
                    if minimum == -1 or dist < minimum:
                        minimum = dist
                        closest = int(item[0])

            final_distance += minimum
            new_coord.append(closest)
            remaining_cities.remove(closest)

        come_back = sqrt((float(coord[new_coord[-1] - 1][1]) - float(coord[new_coord[1] - 1][1])) ** 2 +
                         (float(coord[new_coord[-1] - 1][2]) - float(coord[new_coord[1] - 1][2])) ** 2)
        final_distance += come_back

        result = f"list of indexes of cities sorted by the closest distance {new_coord} " \
                 f"\nGive the total distance of {format(final_distance, '.2f')}"

        return new_coord

    # Distance
    @staticmethod
    def distance(cities, coord):
        path = 0

        for idx, item in enumerate(cities):
            # case we return from last to first city
            if idx == len(cities) - 1:

                dist = sqrt((float(coord[cities[idx] - 1][1]) - float(coord[cities[0] - 1][1])) ** 2 +
                            (float(coord[cities[idx] - 1][2]) - float(coord[cities[0] - 1][2])) ** 2)
                path += dist
            else:
                dist = sqrt((float(coord[cities[idx + 1] - 1][1]) - float(coord[cities[idx] - 1][1])) ** 2 +
                            (float(coord[cities[idx + 1] - 1][2]) - float(coord[cities[idx] - 1][2])) ** 2)
                path += dist

        return format(path, ".2f")

    # Initial population
    @staticmethod
    def population(cities, coords):
        pop = []
        for _ in range(89):
            random.shuffle(cities)
            new = list(cities)
            pop.append(new)

        for _ in range(11):
            greedy_results = GeneticAlgorithm.greedy_algorithm(coords)
            pop.append(greedy_results)

        return pop

    # Fitness function
    @staticmethod
    def fitness(whole_population, coord):
        results = []
        for idx, item in enumerate(whole_population):
            dist = float(GeneticAlgorithm.distance(whole_population[idx], coord))
            results.append([dist, item])

        fittest = sorted(results)[:1]

        print(f"The result with the shortest path: {fittest}")

        return fittest

    # Mutations for the population
    @staticmethod
    def mutations(pop, coord):
        print(f"Population before mutations {pop} has distance: {GeneticAlgorithm.distance(pop, coord)}")
        random_index = random.randint(0, len(pop) - 1)
        random_index_2 = random.randint(0, len(pop) - 1)

        pop[random_index], pop[random_index_2] = pop[random_index_2], pop[random_index]

        print(f"Population after mutations {pop} has distance: {GeneticAlgorithm.distance(pop, coord)}")

        return pop

    @staticmethod
    def inversion(pop, coord):
        rand = get_two_random_items(pop)

        print(f"Population before inversion {pop} has distance: {GeneticAlgorithm.distance(pop, coord)}")

        to_reverse = pop[rand[0]:rand[1]]
        to_reverse.reverse()
        new_pop = pop
        del new_pop[rand[0]:rand[1]]
        new_pop[rand[0]:rand[0]] = to_reverse

        print(f"New population {new_pop} has distance: {GeneticAlgorithm.distance(new_pop, coord)}")

        return new_pop

    @staticmethod
    # find best result out of n species to consider
    def tournament(n, pop, coord):
        pop_to_consider = random.sample(pop, n)
        result = GeneticAlgorithm.fitness(pop_to_consider, coord)
        print(f"Result of the tournament is {result}")
        return result

    @staticmethod
    def croosover(first_parent, second_parent):
        if len(first_parent) != len(second_parent):
            raise Exception("Two objects must be items of the same population, and therefore have the same length!")

        # create two random numbers
        rand = get_two_random_items(first_parent)

        # items to be cut from first parent
        to_cut = first_parent[rand[0]:rand[1] + 1]

        # second parent without items cut from first parent
        after_cut = [num for num in second_parent if num not in to_cut]

        # put cut results in place of smaller index of second parent after deletion
        after_cut.insert(rand[0], to_cut)

        # flatten
        flat = list(flatten(after_cut))

        print(f"Output {flat}")
