class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        res=[]
        for co in count.most_common(k):
            res.append(co[0])
        return res