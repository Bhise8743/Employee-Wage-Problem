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

        Return: None
    """

    ran_int = random.randint(0,1)
    if ran_int == 1:
        print("Employee Present ")
    else:
        print("Employee Not Present ")

if __name__=="__main__":
    print("Welcome To Employee Wage Computation Program ")
    check_attendence()