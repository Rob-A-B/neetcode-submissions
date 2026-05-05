class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        hi=n-1
        lo=0
        
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                lo=mid+1
            if nums[mid]>target:
                hi=mid-1
        return -1
    