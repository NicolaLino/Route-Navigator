from dataRetriever import getGraphPoints
import pandas as pd
import networkx as nx
from heapq import heappush, heappop
from itertools import count
from networkx.algorithms.shortest_paths.weighted import _weight_function




def astar(G, source, target, heuristic=None, weight="weight"):

    if source not in G or target not in G:
        msg = f"Either source {source} or target {target} is not in G"
        raise nx.NodeNotFound(msg)

    if heuristic is None:
        # The default heuristic is h=0 - same as Dijkstra's algorithm
        def heuristic(u, v):
            return 0

    push = heappush
    pop = heappop
    weight = _weight_function(G, weight)

    # The queue stores priority, node, cost to reach, and parent.
    # Uses Python heapq to keep in priority order.
    # Add a counter to the queue to prevent the underlying heap from
    # attempting to compare the nodes themselves. The hash breaks ties in the
    # priority and is guaranteed unique for all nodes in the graph.
    c = count()
    queue = [(0, next(c), source, 0, None)]

    # Maps enqueued nodes to distance of discovered paths and the
    # computed heuristics to target. We avoid computing the heuristics
    # more than once and inserting the node into the queue too many times.
    enqueued = {}
    # Maps explored nodes to parent closest to the source.
    explored = {}

    while queue:
        # Pop the smallest item from queue.
        _, __, curnode, dist, parent = pop(queue)

        if curnode == target:
            path = [curnode]
            node = parent
            while node is not None:
                path.append(node)
                node = explored[node]
            path.reverse()
            return path

        if curnode in explored:
            # Do not override the parent of starting node
            if explored[curnode] is None:
                continue

            # Skip bad paths that were enqueued before finding a better one
            qcost, h = enqueued[curnode]
            if qcost < dist:
                continue

        explored[curnode] = parent

        for neighbor, w in G[curnode].items():
            ncost = dist + weight(curnode, neighbor, w)
            if neighbor in enqueued:
                qcost, h = enqueued[neighbor]
                # if qcost <= ncost, a less costly path from the
                # neighbor to the source was already determined.
                # Therefore, we won't attempt to push this neighbor
                # to the queue
                if qcost <= ncost:
                    continue
            else:
                h = heuristic(neighbor, target)
            enqueued[neighbor] = ncost, h
            push(queue, (ncost + h, next(c), neighbor, ncost, curnode))

    raise nx.NetworkXNoPath(f"Node {target} not reachable from {source}")


# from graph import create_graph

# g = create_graph()
# path_list = astar(g, "Bethlehem", "Nablus", heuristic=None, weight='weight')

# print(path_list)


def BFS(G, source, target):
    
    
    #replace push and pop with heap pop and push, so we can use a priority queue
    push = heappush
    pop = heappop
    #use iterator to count
    c = count()
    fringe = [(next(c), source, 0, None)]
    #dict holding hearistic and lowest cost to reach from src, with key being node name
    enqueued = {}
    #dict holding parent of node, with key being node name
    explored = {}

    while fringe:
        __, curnode, dist, parent = pop(fringe)

        if curnode == target:
            path = [curnode]
            node = parent
            while node is not None:
            #go from parent to parent until we reach the starting node
                path.append(node)
                node = explored[node]
            path.reverse()
            return path
        
        if curnode in explored:
            #this condition means that the node is the src node
            if explored[curnode] is None:
                continue
            #get the heauristic and cost reach of the node
            qcost = enqueued[curnode]
            if qcost < dist:
                continue
            
        #get the parent of the current node
        explored[curnode] = parent

        for neighbor, w in G[curnode].items():
            #get the accumelated cost to reach the neighbor node from the source
            ncost = dist + 1
            if neighbor in enqueued:
                # if we already know a shorter path we can get it from the enqueued queue
                qcost = enqueued[neighbor]
                if qcost <= ncost:
                    continue
            # write new shortest path to reach this node
            enqueued[neighbor] = ncost
            # push the produced values into the priority queue
            # [priority/iteration, node, cost to reach from src, parent node]
            push(fringe, (next(c), neighbor, ncost, curnode))

    raise nx.NetworkXNoPath(f"Node {target} not reachable from {source}")


def greedy(G, source, destination, heuristic=None):
    
    # replace push and pop with heap pop and push, so we can use a priority queue
    push = heappush
    pop = heappop
    
    # use iterator to count
    c = count()
    fringe = [(0, next(c), source, None)]
    
    # dict holding heuristic values, with key being node name
    enqueued = {}
    
    # dict holding the parent of explored nodes, with key being node name
    explored = {}
    
    max_iterations = 100000
    iters = 0

    while fringe:
        
        if iters > max_iterations:
            break
        iters += 1
        
        _, __, current_node, parent = pop(fringe)

        if current_node == destination:
            path = [current_node]
            node = parent
            while node is not None:
                # go from parent to parent until we reach the starting node
                path.append(node)
                node = explored[node]
            path.reverse()
            return path

        if current_node in explored:
            # this condition means that the node is the src node
            if explored[current_node] is None:
                continue
            # get the heuristic and cost reach of the node
            h = enqueued[current_node]

        # get the parent of the current node
        explored[current_node] = parent
        for child, w in G[current_node].items():
            if child in enqueued:
                
                # if the heuristic was already calculated read it from the enqueued queue
                h = enqueued[child]
            else:
                # else calculate heuristic
                h = heuristic(child, destination)

            # save the new heuristic value or the shorter path to reach this node
            enqueued[child] = h
            # push the produced values into the priority queue
            # [priority, iteration, node, cost to reach from src, parent node]
            push(fringe, (h, next(c), child, current_node))
