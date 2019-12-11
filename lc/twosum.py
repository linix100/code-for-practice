class Solutions:
    def twoSum(self, nums, target):
	    mapping={}
	    for i,number1 in enumerate(nums):
	        number2=target-number1
	        if number2 in mapping:
	            return [i,mapping[number2]]
	        else:
	            mapping[number1]=i