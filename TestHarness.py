# ---------------------------------------------------------- #
# Title: TestingHarness.py
# Description: Testing Harness to test DataClasses and ProcessingClasses modules
# ChangeLog (Who,When,What):
# Alex Frain,3.12.2021,Created started script
# ---------------------------------------------------------- #

if __name__ == "__main__":
    from DataClasses import Employee as Emp  # Employee class only
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test data module
print("*** Testing data module ***")
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
objP3 = Emp(3, "Daniel", "Cormier")
lstTable = [objP1, objP2, objP3]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
print("\n*** Testing FileProcessor module ***")
print("Save to File\n")
Fp.save_data_to_file("EmployeeData.txt", lstTable)
print("Read from File")
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test IO module
print("\n*** Testing IO module  ***")
Eio.print_menu_items()  # print menu
Eio.print_current_list_items(lstTable)     # Display current employee list
new_emp = Eio.input_employee_data()    # Add employee
print(new_emp)
choice = Eio.input_menu_options()
print(choice)

