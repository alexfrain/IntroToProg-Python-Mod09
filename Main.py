# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Alex Frain ,03/12/21,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

emp_file_name = "EmployeeData.txt"
emp_lst = []

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
table_lst = Fp.read_data_from_file(emp_file_name)
for row in table_lst:
    emp_lst.append(Emp(row[0], row[1], row[2].strip()))

print(f"{emp_file_name} data loaded.")
Eio.print_current_list_items(emp_lst)

# Show user a menu of options
while True:
    Eio.print_menu_items()

    # Get user's menu option choice
    choice_str = Eio.input_menu_options()

    # Show user current data in the list of employee objects
    if choice_str == "1":
        Eio.print_current_list_items(emp_lst)

    # Let user add data to the list of employee objects
    elif choice_str == "2":
        emp_obj = Eio.input_employee_data()
        emp_lst.append(emp_obj)
        print(f"{emp_obj} added to employee list")

    # let user save current data to file
    elif choice_str == "3":
        if Fp.save_data_to_file(emp_file_name, emp_lst):
            print("Employee list saved to file.")
        else:
            print("Employee list not saved.")

    # Let user exit program
    elif choice_str == "4":
        print("Exiting script. Goodbye!")
        break
# Main Body of Script  ---------------------------------------------------- #