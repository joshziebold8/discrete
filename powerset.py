class PowerSet:
    
    def powerset(self, input_set):
        allSubsets = []
        for i in range(2**len(list(input_set))):
            subset = []
            for j in range(len(list(input_set))):
                if i & 1 << j:
                    subset.append(list(input_set[j]))
            allSubsets.append(subset)
        return set(allSubsets)
