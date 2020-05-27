class Solution(object):
	def threeSum(self, nums):
        	"""
        	:type nums: List[int]
        	:rtype: List[List[int]]
        	"""
        
        	result = {}

        	cptr = 1
        	cnt = 0
        	nums = sorted(nums)
        
        	if len(nums) < 3:
            		return []
        	if nums[0] == nums[len(nums)-1] == 0:
            		return [[0,0,0]]
        
        	while cptr < len(nums)-1:
            		aptr = cptr-1
            		bptr = cptr+1
            
            		while aptr >= 0 and bptr <= len(nums)-1:    
                		if (nums[aptr]+nums[bptr]+nums[cptr] > 0):
                    			aptr -= 1
                    
                		elif (nums[aptr]+nums[bptr]+nums[cptr] < 0):
                    			bptr += 1
                    
                		elif (nums[aptr]+nums[bptr]+nums[cptr] == 0):
                    			result[nums[aptr], nums[bptr], nums[cptr]] = cnt
                    			cnt += 1
                    			aptr -= 1
                    
            		cptr +=1
        
        	return result
        