class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0 #Sets Pointer
        n = len(nums) #Length of Input List 
        for num in nums: #Loops over input list
            if(num != 0): #checks for valid number - a valid number is NOT 0
                nums[j] = num #sets variable at j
                j += 1 #Valuable is now full
                
        for x in range(j,n): #0's out the rest of the element
            nums[x] = 0