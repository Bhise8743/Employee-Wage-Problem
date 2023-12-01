"""

@Author: Omkar Bhise

@Date: 2023-12-01 11:45:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-11-29 1:00:00

@Title :  Employee Wage

"""


import random
wage_per_hr = 20
full_time_wk_hr = 8
part_time_wk_hr = 4

def random_check():
    """
       Description:
           This function use to return the random value 0 or 1

       Parameter:
           None

       Return: int value
       """
    return random.randint(0, 1)


def check_attendence():
    """
        Description:
            This function use to check the  attendence of employee

        Parameter:
            None

        Return: Boolean Value
    """
    ran_int = random_check()
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


    rand_int = random_check()

    if rand_int == 1:
        part_time_wage = wage_per_hr * part_time_wk_hr
        print(f"Employee Doing the part time work it's wage is :  {part_time_wage}")
    else:
        full_time_wage = wage_per_hr * full_time_wk_hr
        print(f"Employee Daily Full Time Wage is : {full_time_wage}")

def main():
    print("Welcome To Employee Wage Computation Program ")

    if check_attendence():
        emp_dly_wage()
    else:
        print("Employee Daily Wage is 0 ")


if __name__=="__main__":
    main()

