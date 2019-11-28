##Problem set 0
import math
def homework_0():
    x = int(input("input value for x"))
    y = int(input("input value for y"))
    z1 = x**y
    z2 = math.log(x,10)
    print('Enter number x:', x)
    print('Enter number y:', y)
    print('x**y = ', z1)
    print('log(x) = ', z2)

homework_0()

##Problem set 1
def hw1_A(annual_salary,save_percentage,total_cost):
    total_saving = 0
    month = 0
    while total_saving - total_cost*0.25<=0:
        total_saving = total_saving + total_saving*0.04/12 + annual_salary*save_percentage/12
        month +=1
    return month


def hw1_B(annual_salary,save_percentage,total_cost,semi_raise):
    total_saving = 0
    month = 0
    while total_saving - total_cost*0.25<=0:
        total_saving = total_saving + total_saving*0.04/12 + annual_salary*save_percentage/12
        month +=1
        if month % 6 ==0:
            annual_salary =annual_salary*(1+semi_raise)
    return month


def hw1_C(annual_salary):
    start = 0
    end = 10000
    save_percentage = 0.5
    step = 0
    while abs(hw1_c_total_saved(annual_salary,save_percentage) - 250000) >=100:
        if hw1_c_total_saved(annual_salary,save_percentage) > 250000:
            end = save_percentage * 10000
        else:
            start = save_percentage * 10000
        save_percentage = int((start + end) / 2) / 10000
        step += 1
    return save_percentage, step

def hw1_c_total_saved(annual_salary,save_percentage):
    total_saving = 0
    for i in range(0,96):
        total_saving = total_saving + total_saving * 0.04 / 12 + annual_salary * save_percentage / 12
        i += 1
        if i % 12 == 0:
            annual_salary = annual_salary * 1.04
    return total_saving

