def BFS(g, s, discovered):
    """
    Perform BFS of the undiscovered portion of Graph g starting at Vertex s.
    discovered is a dictionary mapping each vertex to the edge thatwas used to
    discover it during the BFS(s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the ictionary as a result.
    """
    level = [s]
    while len(level) > 0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v)
        level = next_level