class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        hi=n-1
        lo=0

        while(hi>lo):
            summ= numbers[lo]+numbers[hi]
            if summ==target:
                return [lo+1,hi+1]
            
            if summ<target:
                lo+=1
            if summ>target:
                hi-=1
                