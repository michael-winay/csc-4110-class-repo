import pydoc

class VariableSort():
    """
    this class will sort variables through an add item method
    """
    string_list = []
    float_list = []
    int_list = []

    def __init__(self):
        self.string_list = []
        self.float_list = []
        self.int_list = []

    def addItem(self, var_in):
        try:
            if type(var_in) is str:
                if var_in.isalpha():
                    self.string_list.append(var_in)
                else:
                    print("String must contain only alphabetic characters")
            if type(var_in) is float:
                self.float_list.append(var_in)
            if type(var_in) is int:
                self.int_list.append(var_in)
        except:
            print("Invalid characters")

    def showLists(self):
        print("Strings:", self.string_list)
        print("Floats:", self.float_list)
        print("Ints:", self.int_list)

if __name__ == '__main__':
    """
    Driver code for sorting class
    """
    running = True
    lists = VariableSort()
    test_cases = ['abc', 123, 1.3, 'ABC', 'abc123', 9223372036854775808, '$%&**(&)']
    test_case_iter = 0
    print("Beginning automated tests...")
    while running:
        if test_case_iter < 7:
            print("Automated item being added:", test_cases[test_case_iter])
            lists.addItem(test_cases[test_case_iter])
            lists.showLists()
            test_case_iter += 1

        else:
            data = input("Enter new data to add to lists: ")
            lists.addItem(data)
            lists.showLists()
            exit_prog = input("Continue? y/n: ")
            if exit_prog == "n":
                running = False