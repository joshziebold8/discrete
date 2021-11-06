class Jumble():
	
	def get_total_distinct_combinations(self, input_string):
		import math
		x = 0
		for i in input_string:
			if input_string.count(i) == 1:
				x+=1
		return math.factorial(len(input_string)) / math.factorial(len(input_string)-x)