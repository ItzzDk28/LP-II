def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:          
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

if __name__ == '__main__':

    graph = {
      '1' : ['2','3'],
      '2' : ['4', '5'],
      '3' : ['6','7'],
      '4' : [],
      '5' : [],
      '6' : [],
      '7' : []
    }

    visited1 = set()
    visited2 = set()

    visited1 = [] 
    queue = []  

    print("This is  BFS")
    bfs(visited1, graph, '1')
    print()

    print("This is DFS")
    dfs(visited2, graph, '1')
