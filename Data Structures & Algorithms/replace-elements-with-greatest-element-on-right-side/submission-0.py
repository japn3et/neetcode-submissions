class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i=0
        #for i in arr:
        while i < (len (arr))-1:
            maxRight=0
            for k in range (i + 1, len (arr)) :
                if arr[k] > maxRight:
                    maxRight = arr[k]
                else: 
                    k+=1
            arr[i]=maxRight

            i+=1
        arr[-1]=-1

        return arr
