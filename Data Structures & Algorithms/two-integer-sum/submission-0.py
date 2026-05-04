class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range (0,len(nums)-1):
            for j in range(len(nums)-1,0,-1):
                if i !=j:
                    if nums[i]+nums[j]== target:
                        l.append(i)
                        l.append(j)
                        l.sort()
                        return l
        