class BaseConverter:

	def base_converter(self, num, from_base, to_base):
		sum = 0
		x = len(num)-1
		for i in num: #to decimal
			sum += pow(from_base, x) * int(i)
			x -= 1
		x = sum
		ans = ""
		while x != 0:
			ans += str(x%to_base)
			x/=to_base
		return ans[::-1]
