import random
from math import sqrt


def greedy_algorithm(file_name):
    coord = []

    # result = dict()
    with open(file_name) as file:
        text = file.readlines()[6:]
        for i in text:
            coord.append(tuple(i.split()[0:3]))

    # choosing one random element from which to start
    r = random.randint(1, len(coord) + 1)
    new_coord = [r]

    # list of numbers representing indexes from remaining cities
    remaining_cities = [i for i in range(1, len(coord)+1) if i not in new_coord]

    while len(remaining_cities) > 0:
        # find different distance
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

        new_coord.append(closest)
        remaining_cities.remove(closest)

    result = f"list of indexes of cities sorted by the closest distance {new_coord}"
    print(result)

    return result


# FILES

# greedy_algorithm('files/ali535.tsp') --> in case of this one we should change our function
# to start from 8th line

greedy_algorithm('files/berlin11_modified.tsp')
greedy_algorithm('files/berlin52.tsp')
greedy_algorithm('files/fl417.tsp')
greedy_algorithm('files/kroA100.tsp')
greedy_algorithm('files/kroA150.tsp')
greedy_algorithm('files/kroA200.tsp')
greedy_algorithm('files/nrw1379.tsp')
greedy_algorithm('files/pr2392.tsp')
