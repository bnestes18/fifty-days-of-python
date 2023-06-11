import numpy as np

def flat_list(dim_list):
    arr = np.array(dim_list)
    return arr.reshape(-1)


print("flat_list function:", flat_list([[4,5,6]]))

def your_salary():
    teacher_name = input("Enter the teacher's name: ")
    teacher_periods = input("Enter the teacher's number of periods: ")
    teacher_rate = input("Enter the teacher's rate: ")
    salary = 0

    if int(teacher_periods) > 100:
        extra_periods = int(teacher_periods) - 100
        overtime = 25 * extra_periods
        salary = format(((int(teacher_periods) - extra_periods) * int(teacher_rate)) + overtime, ',')
    else:
        salary = format(int(teacher_periods) * int(teacher_rate), ',')
    
    output = print("""Teacher: {}\nPeriods: {}\nGross Salary: {}""".format(teacher_name, teacher_periods, salary))
    return output

print("your_salary function:", your_salary())

