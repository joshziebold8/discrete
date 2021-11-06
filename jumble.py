class Jumble():
	
	def get_total_distinct_combinations(self, input_string):
		import math
		count = [0] * 26
		for i in range(0, len(input_string)):
			if (input_string[i] >= 'a'):
				count[(ord)(input_string[i]) - 97] += 1
		factorial = 1
		for i in range(0, 26) :
			factorial *= math.factorial(count[i])
		return math.factorial(len(input_string)) / factorial