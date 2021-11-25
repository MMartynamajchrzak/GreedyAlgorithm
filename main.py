from math import sqrt


def read(file_name):
    coord = []
    path = 0
    with open(file_name) as file:
        text = file.readlines()[7:]
        for i in text:
            coord.append(tuple(i.split()[1:3]))

        for idx, item in enumerate(coord):
            if idx == len(coord) - 1:
                break
            dist = sqrt((float(coord[idx+1][0]) - float(item[0]))**2 + (float(coord[idx+1][1]) - float(item[1]))**2)
            path += dist

        print(format(path, ".2f"))
        # doesn't work YET :)

        return text


read('files/ali535.tsp')
read('files/berlin11_modified.tsp')
read('files/berlin52.tsp')
read('files/fl417.tsp')
read('files/kroA100.tsp')
read('files/kroA150.tsp')
read('files/kroA200.tsp')
read('files/nrw1379.tsp')
read('files/pr2392.tsp')
