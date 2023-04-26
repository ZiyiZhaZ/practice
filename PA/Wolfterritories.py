import math

# use this function in the your min_pack_distance function
# c1 stands for coordinate_1, c2 stands for coordinate_2
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def min_pack_distance(pack_coordinates):
    d = []
    for i in range(len(pack_coordinates)):
        for j in range(len(pack_coordinates)):
            if i != j:
                x = distance(pack_coordinates[i],pack_coordinates[j])
                d.append(x)
    return min(d)

packs = [[0.5, 1], [1,11.2], [-1,-1], [13.2,6], [-12.2, 0], [0.7, 2], [2,7]]
print(min_pack_distance(packs))