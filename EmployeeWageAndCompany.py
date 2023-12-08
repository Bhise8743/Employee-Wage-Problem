"""

@Author: Omkar Bhise

@Date: 2023-12-08 9:15:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-08 10:30:00

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
        self.emp_id = 1000 # Emp id start from the company

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
            # inside value Employee Class object is present

    def get_emp(self, emp_id):
        """
           Description:
               this function get the one emp data

           Parameter: self

           Return: None

        """
        try:
            emp: Employee = self.emp_dict.get(emp_id)
            print(f"Emp id : {emp.emp_id} Name is : {emp.emp_name} Total wage : {emp.total_wage}")
        except Exception as ex:
            print("Employee not Present in Company ")

    def update_emp(self, e_id):
        """
           Description:
               this function used update the emp wage

           Parameter: self , Employee object

           Return: None

        """
        try:
            emp: Employee = self.emp_dict.get(e_id)
            emp.emp_wage_of_month()
        except Exception as ex:
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


class MultipleCom:

    def __init__(self):
        self.com_dict = {}

    def add_company(self, com_obj:Company):
        """
           Description:
               this function add new company in function

           Parameter: self , Company object

           Return: None

        """
        self.com_dict.update({com_obj.comp_name : com_obj})

    def get_company(self,com_name):
        """
           Description:
               this function return the company present or not

           Parameter: self , Company name

           Return: Company Object

        """
        return self.com_dict.get(com_name)

    def get_company_with_all_emp_details(self, com_name):
        """
           Description:
               this function print the company name and Emp Present in the company

           Parameter: self , company name

           Return: None

        """
        com_obj:Company = self.com_dict.get(com_name)
        if com_obj:
            print(f"{com_obj.comp_name} and Total Employees in com {len(com_obj.emp_dict) } ")
            com_obj.get_all_emp_details()

    def get_all_com_details(self):
        """
           Description:
               this function print the all Company names and Employee present inside the company

           Parameter: self , Employee object

           Return: None

        """

        for key, value in self.com_dict.items():
            print(f"Company Name : {key} Total Employees in com {value.emp_id - 1000}")

    def remove_company(self, com_name):
        """
           Description:
               this function used to remove the Company for the multiple company class

           Parameter: self , Employee object

           Return: None

        """
        try:
            self.com_dict.pop(com_name)
        except Exception as ex:
            print("Company is not present ")


def main():
    """
       Description:
           this function create a class object and call there methods

       Parameter: self , Employee object

       Return: None

    """

    m_com = MultipleCom()
    while True:
        try:
            user_choice = int(input(f"""Enter the choice 
                            1. Add Emp details 
                            2. get Emp Details
                            3. get All emp details
                            4. Update Emp details
                            5. Remove emp form Company
                            6. Get Comp with all Epm details
                            7. Get all Company details
                            8. Remove Company form Multiple Company
                            9. exist
            """))

            match user_choice:
                case 1:
                    com_name = input("Enter the company name ")
                    com = m_com.get_company(com_name)
                    if com is None:
                        com = Company(com_name)

                    name = input("Enter the employee name ")
                    wage_per_hr = int(input("Enter the wage per hours "))
                    emp_obj = Employee(com.emp_id, name, wage_per_hr, 4, 8, 100, 20)
                    com.emp_id += 1
                    emp_obj.emp_wage_of_month()
                    com.add_employee(emp_obj)

                    m_com.add_company(com)
                case 2:
                    com = input("Enter the company name ")
                    com = m_com.get_company(com_name)
                    e_id = int(input(f"Enter the employee id between 1000 to {com.emp_id - 1} "))
                    com.get_emp(e_id)

                case 3:
                    com_name = input("Enter the company name ")
                    com = m_com.get_company(com_name)
                    com.get_all_emp_details()
                case 4:
                    com_name = input("Enter the company name ")
                    com = m_com.get_company(com_name)
                    e_id = int(input(f"Enter the employee id between 1000 to {com.emp_id - 1} "))
                    com.update_emp(e_id)
                case 5:
                    com_name = input("Enter the company name ")
                    com = m_com.get_company(com_name)
                    e_id = int(input(f"Enter the employee id between 1000 to {com.emp_id - 1} "))
                    com.remove_emp(e_id)
                case 6:
                    com_name = input("Enter the company name ")
                    m_com.get_company_with_all_emp_details(com_name)
                case 7:
                    m_com.get_all_com_details()
                case 8:
                    com_name = input("Enter the company name ")
                    m_com.remove_company(com_name)
                case 9:
                    break
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    main()
