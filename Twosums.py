class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_hashmap = {}
        for index, num in enumerate(nums): 
            """
            new_hashmap = {index:num}
            this is wrong because new hashmap is gonna reset 
            after each iteration so it needs to be outside of the loop

            """
            'index_list = []'
            complement = target - num
            if complement in new_hashmap:
                [new_hashmap[complement], index]
                complement_index = new_hashmap[complement]
                'index_list.append(complement_index)'
                'index_list.append(new_hashmap[num])'
                return [complement_index, index]
            else:
                new_hashmap[num] = index
        return new_hashmap
              
                
            
        
        