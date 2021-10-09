class Largest_Number:

    def get_largest_number(self, input_list):
        max = input_list[0]
        for i in range(0, len(input_list)):
            if input_list[i] > max:
                max = input_list[i]
        return max
