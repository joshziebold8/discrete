class PowerSet:
    
    def powerset(self, input_set):
        allSubsets = []
        inputList = list(input_set)
        for i in range(2**len(inputList)):
            subset = []
            for j in range(len(inputList)):
                if i & 1 << j:
                    subset.append(inputList[j])
            allSubsets.append(subset)
        return allSubsets
