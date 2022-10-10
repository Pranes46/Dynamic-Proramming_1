class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []        #assigning dp array
        if len(nums)==1:     #if length of the array is one we have to return index 0
            return nums[0]
        dp.append(nums[0])    #we have to append the nums[0] in the dp array
        dp.append(max(nums[0],nums[1]))  #comparing the first two indexes and appending the max
        
        for i in range(2,len(nums)):   #iterating all the nums in list
            dp.append(max((nums[i]+dp[i-2]),dp[i-1]))  #appending the max element between curent element + dp array's previous element's before element with dp array's last element
        return dp[-1]#returning the last element in dp array
            
           