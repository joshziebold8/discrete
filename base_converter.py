class BaseConverter:

	def base_converter(self, num, from_base, to_base):
		sum = 0
		x = len(num)-1
		for i in num: #to decimal
			print(x)
			print(ord(i))
			sum += pow(from_base, x) * ord(i)
			print(sum)
			x -= 1
		return sum
