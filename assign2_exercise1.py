import statistics as s

class List_Mean:
    num_list = []

    def set_list(self,list): # sets list
        self.num_list = list

    def get_list(self): # returns list
       return self.num_list

    def calc(self): # calc avg of string list
        for i in range(0, len(self.num_list)):
            try: # try to convert sting num to float
                self.num_list[i] = float(self.num_list[i])
            except ValueError: # if no number
                return
        return s.mean(self.num_list) #calc avg


input_string = input("Please enter numbers separated by space:\n")
list = input_string.split()

average = List_Mean()
average.set_list(list)
print("Your list is:", average.get_list())
avg_result = average.calc()
if avg_result is not None:
    print("The average is", avg_result)
else:
    print("Please give only numbers to calculate the average.")
