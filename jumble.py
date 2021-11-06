class Jumble():
	
	def get_total_distinct_combinations(self, input_string):
		import math
		x = 0
		temp = ""
		for i in input_string:
			if input_string.count(i) == 1 or temp.count(i) == 0:
				temp += i
				x+=1
		print(temp)
		return math.factorial(len(input_string)) / math.factorial(len(input_string)-x)