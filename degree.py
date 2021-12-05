class Graph():

	def get_degrees(self, A):
		''' A here is the adjacency matrix '''
		out = [len(A)]
		inD = [len(A)]
		ans = ''
		for i in range(len(A)):
			for j in range(len(A)):
				if A[i][j] == 1:
					out[i] += 1
					inD[j] += 1
			ans += "(" + out[i] + "," + inD[i] + "),"	
		return ans