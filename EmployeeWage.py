"""

@Author: Omkar Bhise

@Date: 2023-12-01 11:45:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-11-29 1:00:00

@Title :  Employee Wage

"""


import random
def check_attendence():
    """
        Description:
            This function use to check the  attendence of employee

        Parameter:
            None

        Return: Boolean Value
    """

    ran_int = random.randint(0,1)
    if ran_int == 1:
        print("Employee Present ")
        return True
    else:
        print("Employee Not Present ")

def emp_dly_wage():
    """
        Description:
            This function use to Calculate the Daily Employee Wage

        Parameter:
            None

        Return: None
    """
    wage_per_hr = 20
    working_hr = 8
    wage = wage_per_hr * working_hr
    print("Employee Daily wage is : ", wage)


if __name__=="__main__":
    print("Welcome To Employee Wage Computation Program ")

    if check_attendence():
        emp_dly_wage()
    else:
        print("Employee Daily Wage is 0 ")
