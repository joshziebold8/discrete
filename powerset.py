class PowerSet:
    
    def powerset(self, input_set):
        allSubsets = []
        for i in range(2**len(input_set)):
            subset = []
            for j in range(len(input_set)):
                if i & 1 << j:
                    subset.append(input_set[j])
            allSubsets.append(subset)
        return allSubsets
