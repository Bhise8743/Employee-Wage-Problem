"""

@Author: Omkar Bhise

@Date: 2023-12-05 12:15:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-05 12:30:00

@Title :  Employee Wage using class and methods

"""
import random


class Employee:

    def __init__(self,emp_name,wage_per_hr,full_time_hr,part_time_hr):

        self.wage_per_hr = wage_per_hr
        self.full_time_hr = full_time_hr
        self.part_time_hr = part_time_hr
        self.emp_name= emp_name

    def emp_daily_wage(self):
        """
           Description:
               this function calculate employee daily wage

           Parameter: self

           Return: None

        """
        wage = 0
        work_type = random.randint(0, 1)
        if work_type == 0:  # full time work
            wage = self.wage_per_hr * self.full_time_hr

        else:  # part-time work
            wage = self.wage_per_hr * self.part_time_hr

        print(f"{self.emp_name} Daily wage is : {wage} \n")

    def emp_wage_for_a_month(self):
        """
           Description:
               this function calculate wage for a month

           Parameter: self

           Return: None

        """
        wage = 0
        part_tm_day = 0
        full_tm_day = 0

        # working days per months is 20
        for i in range(20):
            abc = random.randint(0, 1)
            if abc == 0:  # percent
                work_type = random.randint(0, 1)
                if work_type == 0:  # Full time work
                    wage += self.wage_per_hr * self.full_time_hr
                    full_tm_day += 1
                else:
                    wage += self.wage_per_hr * self.part_time_hr
                    part_tm_day += 1
            else:
                pass

        print(f"{self.emp_name} wage for Month is : {wage} \nEmp work part time {part_tm_day} days and full time {full_tm_day} days ,in the working 20 days \n")

    def cal_wage_till_condition(self):
        """
           Description:
               this function calculate the employee wage till the condition

           Parameter: self

           Return: None

        """
        wage = 0
        wk_days = 0
        wk_hr = 0
        pt_wk_days = 0
        ft_wk_days = 0

        while wk_hr < 100 and wk_days < 20:

            working_or_not = random.randint(0, 1)

            if working_or_not == 0:  # working
                wk_days += 1
                work_type = random.randint(0, 1)

                if work_type == 0:  # full time work
                    ft_wk_days += 1
                    wk_hr += self.full_time_hr
                    wage += self.wage_per_hr * self.full_time_hr
                else:
                    pt_wk_days += 1
                    wk_hr += self.part_time_hr
                    wage += self.part_time_hr
            else:  # Employee not working
                pass

        print(f"{self.emp_name} Working hours : {wk_hr} and Working Days : {wk_days}")
        print(f"Part time work days : {pt_wk_days} Full time work days {ft_wk_days} \n")


def main():
    """
       Description:
           this function call the employee class methods

       Parameter: self

       Return: None

    """

    emp_obj = Employee("Omkar" ,20,8,4)

    emp_obj.emp_daily_wage()
    emp_obj.emp_wage_for_a_month()
    emp_obj.cal_wage_till_condition()


if __name__ == '__main__':
    main()



