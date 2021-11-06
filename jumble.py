class Jumble():
	
	def get_total_distinct_combinations(self, input_string):
		import math
		str = input_string.lower()
		count = [0] * 26
		for i in range(0, len(str)):
			if (str[i] >= 'a'):
				count[(ord)(str[i]) - 97] += 1
		factorial = 1
		for i in range(0, 26) :
			factorial *= math.factorial(count[i])
		return math.factorial(len(str)) / factorial