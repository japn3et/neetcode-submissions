class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mydict={}
        for item in nums:
            if item not in mydict:
                mydict[item]=1
            elif item in mydict:
                mydict[item]+=1
        
        #return max(mydict.values())
        return max(mydict , key=mydict.get)