import tarfile
import networkx as nx
from dataRetriever import getGraphPoints
import matplotlib.pyplot as plt


def create_graph(cost_limit=10000):
    graph, points = getGraphPoints()
    g = nx.Graph()
    city = []
    # for key, _ in points.items():
    #     city.append(key)

    for key, val in graph.items():
        g.add_node(
            key,
            latitude=points[key][0],
            longitude=points[key][1],
            pos=(points[key][0], points[key][1])
        )
    for key, val in graph.items():
        city.append(key)
        for k, i in val.items():
            src_city = key
            target_city = k
            # print(key, k, i)
            cost = i.split('+')
            if len(cost) != 1 and k in city:
                ariel_cost = cost[0]
                walking_cost = cost[1]
                driving_cost = cost[2]
                if int(driving_cost) != 10000:
                    #print(key, k, ariel_cost, walking_cost, driving_cost)
                    g.add_edge(src_city, target_city, ariel=ariel_cost,
                               walking=walking_cost, driving=driving_cost)
    nx.draw(g, with_labels=True)
    # plt.savefig("f3.png")
    return g, points
