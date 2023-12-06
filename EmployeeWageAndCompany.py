"""

@Author: Omkar Bhise

@Date: 2023-12-05 12:15:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-06 04:30:00

@Title :  Employee Wage and Company using class and methods

"""
import random


class Employee:

    def __init__(self, emp_id, emp_name, wage_per_hr, pt_wk_hr, ft_wk_hr, max_wk_hr, max_wk_days):
        """
           Description:
               this is a constructor used to take input from the current object and make globle variable for the object

           Parameter: self emp_id, emp_name, wage_per_hr, pt_wk_hr, ft_wk_hr, max_wk_hr, max_wk_days

           Return: None

        """
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.wage_per_hr = wage_per_hr
        self.pt_wk_hr = pt_wk_hr
        self.ft_wk_hr = ft_wk_hr
        self.max_wk_hr = max_wk_hr
        self.max_wk_days = max_wk_days
        self.total_wage = 0
        self.working_days = 0
        self.wk_hr = 0
        self.pt_tm_wk_days = 0
        self.fl_tm_wk_days = 0

    def emp_wage_of_month(self):
        """
           Description:
               this function calculate wage of emp for a month

           Parameter: self

           Return: None

        """

        wk_days = 0

        while self.wk_hr < self.max_wk_hr and wk_days < self.max_wk_days:
            atd = random.randint(0, 1)  # Attendence
            wk_days += 1
            if atd == 0:  # Emp Percent

                work_type = random.randint(0, 1)
                if work_type == 0:  # Full time work
                    self.total_wage += self.wage_per_hr * self.ft_wk_hr
                    self.wk_hr += self.ft_wk_hr
                    self.pt_tm_wk_days += 1

                else:  # Emp part-time work
                    self.total_wage += self.wage_per_hr * self.pt_wk_hr
                    self.wk_hr += self.pt_wk_hr
                    self.fl_tm_wk_days += 1
            else:  # Emp Absent in working days
                pass


class Company:

    def __init__(self, comp_name):
        self.comp_name = comp_name
        self.emp_dict = {}

    def add_employee(self, emp_obj: Employee):
        """
           Description:
               this function used to add new emp in the company

           Parameter: self , Employee object

           Return: None

        """
        self.emp_dict.update({emp_obj.emp_id: emp_obj})  # making the emp_id as a KEY and push Emp data in dict

    def get_all_emp_details(self):
        """
           Description:
               this function get the all emp data

           Parameter: self

           Return: None

        """
        for key, value in self.emp_dict.items():  # items take a key value pairs
            print(f"Emp_id : {key} Name : {value.emp_name} Total wage : {value.total_wage} PT : {value.pt_tm_wk_days} FT : {value.fl_tm_wk_days} WH : {value.wk_hr}")
            # inside value Employee Class object is persent

    def get_emp(self, emp_id):
        """
           Description:
               this function get the one emp data

           Parameter: self

           Return: None

        """
        emp: Employee = self.emp_dict.get(emp_id)
        if emp:
            print(f"Emp id : {emp.emp_id} Name is : {emp.emp_name} Total wage : {emp.total_wage}")
        else:
            print("Employee not Present ")

    def update_emp(self, e_id):
        """
           Description:
               this function used update the emp wage

           Parameter: self , Employee object

           Return: None

        """
        emp: Employee = self.emp_dict.get(e_id)
        if emp:
            emp.emp_wage_of_month()
        else:
            print("Employee not Present ")

    def remove_emp(self, emp_id):
        """
           Description:
               this function used to remove emp from the company

           Parameter: self , Employee object

           Return: None

        """
        try:
            self.emp_dict.pop(emp_id)
        except Exception as ex:
            print("Employee not present ")


def main():
    """
       Description:
           this function create a class object and call there methods

       Parameter: self , Employee object

       Return: None

    """
    com1 = Company("TCS")

    emp_id = 1000
    while True:
        user_choice = int(input(f"""Enter the choice 
                        1. Add Emp details 
                        2. get Emp Details
                        3. get All emp details
                        4. Update Emp details
                        5. Remove emp form {com1.comp_name}
                        6. exist
        """))

        match user_choice:
            case 1:
                name = input("Enter the employee name ")
                wage_per_hr = int(input("Enter the wage per hours "))
                emp_obj = Employee(emp_id, name, wage_per_hr, 4, 8, 100, 20)
                emp_id += 1
                emp_obj.emp_wage_of_month()
                com1.add_employee(emp_obj)
            case 2:
                e_id = int(input(f"Enter the employee id between 1000 to {emp_id - 1} "))
                com1.get_emp(e_id)
            case 3:
                com1.get_all_emp_details()
            case 4:
                e_id = int(input(f"Enter the employee id between 1000 to {emp_id -1} "))
                com1.update_emp(e_id)
            case 5:
                e_id = int(input(f"Enter the employee id between 1000 to {emp_id - 1} "))
                com1.remove_emp(e_id)
            case 6:
                break


if __name__ == '__main__':
    main()
