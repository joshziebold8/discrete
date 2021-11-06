class Jumble():
	
	def get_total_distinct_combinations(self, input_string):
		import math
		str = input_string.lower()
		x = -1
		temp = ""
		for i in str:
			if str.count(i) == 1 or temp.count(i) == 0:
				temp += i
				x+=1
		print(x, len(str))
		return math.factorial(len(str)) / math.factorial(len(str)-x)