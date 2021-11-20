class EquivalenceRelation():
	
	def check_equivalence(self, relation_members):
		reflexive = True
		symmetric = True
		transitive = True
		set = {0, 1, 2, 3}
		for i in set: #reflexive
			if (i, i) not in relation_members:
				reflexive = False

		for i, j in relation_members: #symmetric
			if (j, i) not in relation_members:
				symmetric = False

		for i in set:
			for j in set:
				if (i, j) in relation_members:
					for x in set:
						if (j, x) in relation_members and (i, x) not in relation_members:
							transitive = False


		if(reflexive and symmetric and transitive):
			return True
		return False