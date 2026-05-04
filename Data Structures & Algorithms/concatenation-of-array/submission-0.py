class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        i=0
        while i!=2: 
            ans.extend(nums)
            i+=1
        return ans