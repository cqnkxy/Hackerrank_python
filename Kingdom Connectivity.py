"""https://www.hackerrank.com/challenges/kingdom-connectivity

I just can't merge two loops into one. I have to first find the
paths without considering the loop in the path that can lead us to
the goal. Then decide whether or not there is a loop including the path.
As one can see the two functions are almost identical.
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections


N, M = map(int, raw_input().strip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, raw_input().strip().split())
    graph[x].append(y)


memo1 = {}


def find_path(cur, visited, success_cities):
    if cur == N:
        success_cities |= visited
        return 1
    if cur in visited:
        return 0
    if cur in memo1:
        ret = memo1[cur]
        if ret:
            success_cities |= visited
        return ret
    visited.add(cur)
    cnt = 0
    for nxt in graph[cur]:
        cnt += find_path(nxt, visited, success_cities)
    visited.discard(cur)
    memo1[cur] = cnt
    return cnt


memo2 = {}


def find_loop(cur, visited, success_cities):
    if cur == N:
        return False
    if cur in visited:
        return cur in success_cities
    if cur in memo2:
        return memo2[cur]
    visited.add(cur)
    loop = False
    for nxt in graph[cur]:
        loop |= find_loop(nxt, visited, success_cities)
        if loop:
            break
    visited.discard(cur)
    memo2[cur] = loop
    return loop

success_cities = set()
ans = find_path(1, set(), success_cities)
loop = find_loop(1, set(), success_cities)
if loop and ans:
    print "INFINITE PATHS"
else:
    print ans % 10**9
