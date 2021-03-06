import numpy as np
COST = 2


def levenshtein_ratio_and_distance(s, t, c=COST):
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows, cols), dtype=int)


    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i
            distance[0][k] = k


    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = c
            distance[row][col] = min(distance[row-1][col] + 1,
                                 distance[row][col-1] + 1,
                                 distance[row-1][col-1] + cost)

    print(f"The strings are {distance[row][col]} edits away", ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t)))


Str1 = "ABC efg."
Str2 = "ABc efG"
levenshtein_ratio_and_distance(Str1, Str2)

