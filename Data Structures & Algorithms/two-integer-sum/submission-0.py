class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        hashmap={}
        for i,v in enumerate(nums):
            comp=target-v
            if v in hashmap:
                return [hashmap[v],i]
            hashmap[comp]=i
        print(hashmap)
        return res
        