from collections import deque
n, m, p = map(int, input().split())
visited = [False for _ in range(n+1)]
adj_list = [[] for _ in range(n+1)]
# adj_list[i] means all node which are connected to ith node
# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
for _ in range(m):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)
# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
# for i in range(len(adj_list)):
#     adj_list[i] = sorted(adj_list[i], reverse=True)
# [[], [4, 3, 2], [4, 1], [4, 1], [3, 2, 1]]
# DFS
q = deque()
q.append(p)
# while q:
#     node = q.pop()
#     print(f'{node} popped')
#     if visited[node]:
#         print(f'{node} already visited')
#         continue
#     else:
#         visited[node] = True
#         print(f'{node} is not been visited')
#         print(node)
#     for connected_node in adj_list[node]:
#         print(f'Append {connected_node} from parent node {node} to deque')
#         q.append(connected_node)

# BFS
q = deque()
q.append(p)
while q:
    node = q.popleft()
    if visited[node]:
        continue
    else:
        visited[node] = True
        print(node)
    for connected_node in adj_list[node]:
        q.append(connected_node)