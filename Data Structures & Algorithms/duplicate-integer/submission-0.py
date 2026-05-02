class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #input array
        #output boo

        dicionario={}
        for i,num in enumerate(nums):
            dicionario[num]=i
        
        for i,v in enumerate(dicionario.values()):
            if i!=v:

                return True
        
        print()
        return False
        