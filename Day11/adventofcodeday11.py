import sys

def solve():
    graph = {}

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line: 
                continue
            
            parts = line.split(": ")
            source = parts[0]
            
            if len(parts) > 1:
                destinations = parts[1].split(" ")
                graph[source] = destinations
            else:
                graph[source] = []

    buh = {}

    def count_paths(current_node):
        if current_node == 'out':
            return 1
        
        if current_node not in graph:
            return 0
        
        if current_node in buh:
            return buh[current_node]
        
        total_paths = 0
        for next in graph[current_node]:
            total_paths += count_paths(next)
        
        buh[current_node] = total_paths
        return total_paths

    result = count_paths('you')

    print(f"Result: {result}")

if __name__ == "__main__":
    solve()