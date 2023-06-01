def DFS(G):
    global time
    for u in G:
        u['p'] = -1
        u['visited'] = False
        u['time_1'] = None
        u['time_2'] = None

    time = 0
    for u in G:
        if not u['visited']:
            DFS_Explore(u, G)

def DFS_Explore(u, G):
    global time
    time += 1
    u['time_1'] = time
    u['visited'] = True

    for v in G[u]:
        if not v['visited']:
            v['p'] = u
            DFS_Explore(v, G)

    time += 1
    u['time_2'] = time

# Przykładowe wywołanie DFS
graph = {
    'V0': [{'p': None, 'visited': False}, 'V1', 'V5'],
    'V1': [{'p': None, 'visited': False}, 'V0', 'V2', 'V3'],
    'V2': [{'p': None, 'visited': False}, 'V1', 'V3', 'V4'],
    'V3': [{'p': None, 'visited': False}, 'V1', 'V2'],
    'V4': [{'p': None, 'visited': False}, 'V2', 'V5', 'V6'],
    'V5': [{'p': None, 'visited': False}, 'V0', 'V4'],
    'V6': [{'p': None, 'visited': False}, 'V4']
}

time = 0
DFS(graph)
