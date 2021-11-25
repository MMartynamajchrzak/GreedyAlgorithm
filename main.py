import math


def read(file_name):
    lon_lat = []
    coord = []
    with open(file_name) as file:
        text = file.readlines()[7:]
        for i in text:
            coord.append(tuple(i.split()[1:3]))

        for idx, item in enumerate(coord):
            if idx == len(coord) - 1:
                break
            lon_diff = (int(float(item[0])) - int(float(coord[idx+1][0])))**2
            lat_diff = (int(float(item[1])) - int(float(coord[idx+1][1])))**2
            leng = lon_diff - lat_diff
            if leng > 0:
                dist = math.sqrt(leng)
        # doesn't work YET :)

        return text


# read('files/ali535.tsp')
read('files/berlin11_modified.tsp')
# read('files/berlin52.tsp')
# read('files/fl417.tsp')
# read('files/kroA100.tsp')
# read('files/kroA150.tsp')
# read('files/kroA200.tsp')
# read('files/nrw1379.tsp')
# read('files/pr2392.tsp')
