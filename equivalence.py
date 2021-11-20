class EquivalenceRelation():

	def check_equivalence(self, relation_members):
		reflexive = True
		symmetric = True
		transitive = True
		for i in relation_members: #reflexive
			if not relation_members(i, i):
				reflexive = False

		for i in relation_members: #symmetric
			for j in relation_members:
				if relation_members(i, j) != relation_members(i, j):
					symmetric = False

		for i in relation_members:
			for j in relation_members:
				for x in relation_members:
					if (relation_members(i, j) and relation_members(j, x)) and (not relation_members(i, x)):
						transitive = False


		if(reflexive and symmetric and transitive):
			return True
		return False