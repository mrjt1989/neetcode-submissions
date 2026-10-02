class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dictionary of nums and their counts
        num_count_dict = dict()
        for num in nums:
            num_count_dict[num] = 1 + num_count_dict.get(num, 0)
        
        count_buckets = []
        count_list = []
        for key in num_count_dict.keys():
            count_list.append(num_count_dict[key])
            count_buckets.append([num_count_dict[key], key])
            
        count_buckets.sort(key=lambda x: x[0])
        print(count_buckets)
        
        k_list = []
        while k > 0:
            highest_count = count_buckets.pop()
            print(highest_count)
            highest_count_num = highest_count[1]
            k_list.append(highest_count_num)
            k = k - 1
        return k_list
        
        
        

            
            
            
            
        
        