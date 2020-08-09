import numpy as np


def basicFeaturesExtract(data):
    features = []
    for i in range(len(data)):
        row = []
        for j in range(len(data[0])):
            if data[i][j] > 0:
                row.append(1)
            else:
                row.append(0)
        features.append(row)
    return np.array(features)


def advancedFeaturesExtract(data):
    # find cycles in the image using DFS
    width = len(data)
    height = len(data[0])
    # cycle cnt
    cycle = -1
    features = basicFeaturesExtract(data)
    # visited->1;not->0
    visited = np.empty_like((height, width))
    visited = np.array(features)
    while not (np.count_nonzero(visited) == visited.size):
        open = []
        # get next 0
        open.append(np.unravel_index(visited.argmin(), visited.shape))
        while not (len(open) == 0):
            current = open.pop()
            visited[current[0]][current[1]] = 1
            neighbors = getNeighbor(current, width, height, visited)
            for nb in neighbors:
                if not features[nb[0]][nb[1]]:
                    open.append(nb)
        cycle += 1
    cyclef = np.zeros((1, width))
    for i in range(cycle):
        cyclef[0][i] = 1
    features = np.vstack((features, cyclef))
    return features


def getNeighbor(s, w, h, visited):
    x, y = s
    neighbors = []
    if isValid((x - 1, y), w, h) and not visited[x - 1][y]:
        neighbors.append((x - 1, y))
    if isValid((x + 1, y), w, h) and not visited[x + 1][y]:
        neighbors.append((x + 1, y))
    if isValid((x, y - 1), w, h) and not visited[x][y - 1]:
        neighbors.append((x, y - 1))
    if isValid((x, y + 1), w, h) and not visited[x][y + 1]:
        neighbors.append((x, y + 1))
    return neighbors


def isValid(s, w, h):
    # distinguish whether out of boundary
    x, y = s
    return 0 <= x < h and 0 <= y < w
