class Jumble():
	
	def get_total_distinct_combinations(self, input_string):
		import math
		str = input_string.lower()
		x = 0
		y = 0
		temp = ""
		for i in str:
			if str.count(i) == 1 or temp.count(i) == 0:
				temp += i
				x+=1
			if temp.count(i) > 1:
				y += 1
		print(x, len(str))
		return (math.factorial(len(str)) / math.factorial(len(str)-x)) / y