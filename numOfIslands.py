def numIslands(self, grid):
	"""
        :type grid: List[List[str]]
        :rtype: int
        """
        
        ones = set()
        ans = 0
        
        i = 0
        
        while i < len(grid):
        	j=0
        	while j < len(grid[i]):
                	if grid[i][j] == '1' and (i,j) not in ones:
                    		ones.add((i,j))
                    		self.getIsland(i+1, j, grid, ones)
                    		self.getIsland(i, j+1, grid, ones)
                    		ans += 1
                	j += 1
        	i+=1
            
        return ans
        
def getIsland(self, i, j, grid, ones):
	if (i,j) not in ones:
        	if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i]) and grid[i][j] == '1':
                	ones.add((i,j))
                	self.getIsland(i+1, j, grid, ones)
                	self.getIsland(i, j+1, grid, ones)
                	self.getIsland(i-1, j, grid, ones)
                	self.getIsland(i, j-1, grid, ones)
            