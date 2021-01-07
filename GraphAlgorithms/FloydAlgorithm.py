nV = 4
INF = 999


def floyd_warshall(graph):
    distance = graph
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print(distance)


G = [[0, 3, INF, 5], [2, 0, INF, 4], [INF, 1, 0, INF], [INF, INF, 2, 0]]
floyd_warshall(G)
