visited = {}
        
keys = [0]
        
while keys:
	index = keys.pop()
        if index not in visited:
        	visited[index] = True
                keys = keys + rooms[index]   
        
return len(visited) == len(rooms)