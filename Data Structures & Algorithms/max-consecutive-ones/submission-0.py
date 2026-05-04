class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter=0
        l1=[]
        for i in range (0,len(nums)):
            if nums[i] == 1:
                counter +=1     
            else:
                l1.append(counter)
                counter = 0
        l1.append(counter)
        return max(l1)