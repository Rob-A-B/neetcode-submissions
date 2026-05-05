def bs(l,r,nums,target):
       
        if l>r:
            return -1
        
        m=(l+r)//2

        if nums[m]==target:
            return m
        if nums[m]>target:
            return bs(l,m-1,nums,target)
        if nums[m]<target:
            return bs(m+1,r,nums,target)
class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
 
        
        return bs(0,len(nums)-1,nums,target)
