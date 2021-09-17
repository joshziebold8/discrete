class CartesianProduct:

	def get_cartesian_product(self, A, B, C):
		listOfLists = []
		for i in range(len(A)):
			for j in range(len(B)):
				for k in range(len(C)):
					temp = [A[i], B[j], C[k]]
					listOfLists.append(temp)
		return listOfLists