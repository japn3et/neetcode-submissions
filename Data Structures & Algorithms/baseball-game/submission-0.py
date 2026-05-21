class Solution:
    def calPoints(self, operations: List[str]) -> int:
        count = []
        for i in operations: 
            if i == '+':
                j= count[-1]+ count[-2]
                count.append(j)
            elif i == 'C':
                count.pop()
            elif i == 'D':
                dbl= count[-1]*2
                count.append(dbl)
            else:
                count.append(int(i))
        
        sum=0    
        for i in count:
            sum += i
        return sum



