import hashlib

inf = float("inf")
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return node

def dijkstra_algorithm(graph, costs, parents):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys:
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node()
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = inf

parents = {}
parents["a"] = "start"
parents["b"] = None

dijkstra_algorithm(graph, costs, parents)

print("Cost from the start to each node:")
print(costs)
