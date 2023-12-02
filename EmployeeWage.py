"""

@Author: Omkar Bhise

@Date: 2023-12-01 05:45:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-02 10:30:00

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


def UsingSwitchCase():  # UC 4
    """
        Description:
            This function use to Calculate the Daily full time or part-time wage

        Parameter:
            None

        Return: None
    """

    atd = random_check()
    match atd:
        case 0:
            part_time_wk_wage = wage_per_hr * part_time_wk_hr
            print(f"Employee Doing Part Time work it's wage is {part_time_wk_wage}")
        case 1:
            full_time_wk_wage = wage_per_hr * full_time_wk_hr
            print(f"Employee Doing Full time work it's wage is : {full_time_wk_wage}")
        case 2:
            print("Employee Absent ")


def Cal_wage_for_month():  # UC 5
    """
           Description:
               This function use to Calculating the wage for the month

           Parameter:
               None

           Return: None
       """
    wage_for_month = 0
    for i in range(20):
        if random_check():
            if random_check():  # if true then Eml Doing the part-time work
                print(f"day {i + 1} working part-time wage is : 4")
                wage_for_month += wage_per_hr * part_time_wk_hr
            else:
                print(f"day {i + 1} Employee working full time wage is : 8")
                wage_for_month += wage_per_hr * full_time_wk_hr
        else:
            print(f"day {i + 1} Employee Absent ")
    print(f"Total wage of 20 days {wage_for_month}")


def total_wk_hr_or_days_reached_for_month():  # UC 6
    """
           Description:
               This function use to Calculate Wages till a condition of total working
           #   working hours or days is reached for a month

           Parameter:
               None

           Return: None
       """
    wage = 0
    wk_hr = 0
    day = 1
    part_time_wr_days = 0
    full_time_work_days = 0
    while wk_hr <= 100 and day <= 20:
        if random_check():  # it checks the employee percent or not
            day += 1
            if random_check():  # it checks the employee doing part-time work
                wage += wage_per_hr * part_time_wk_hr
                part_time_wr_days += 1
                wk_hr += 4
            else:
                wage += wage_per_hr * full_time_wk_hr
                full_time_work_days += 1
                wk_hr += 8
    print(f"part time work days {part_time_wr_days} full time work days {full_time_work_days}")
    print(f"total part time work hours {part_time_wr_days * 4} or calculated {part_time_wk_hr}")
    print(f"total full time work hours {full_time_work_days * 8} or calculated {full_time_wk_hr}")
    total = part_time_wr_days * 4
    total += full_time_work_days * 8
    print(f"total is : {total * 20}")
    print(f"100 working hours or {day} days works {wk_hr * 20}")


def main():
    """
           Description:
               This function use to call the other function and perform the task

           Parameter:
               None

           Return: None
       """

    print("Welcome To Employee Wage Computation Program ")

    # if check_attendence():
    #     emp_dly_wage()
    # else:
    #     print("Employee Daily Wage is 0 ")

    # UsingSwitchCase()

    # Cal_wage_for_month()

    total_wk_hr_or_days_reached_for_month()


if __name__ == "__main__":
    main()
