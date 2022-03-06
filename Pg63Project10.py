hourly = float(input("Enter the hourly wage for work: "))
regular= int(input("Enter the total number of regular hours worked: "))
overtime = int(input("Enter the total overtime hours worked: "))
OvertimePay = overtime * (1.5 * hourly)
TotalWeekPay = hourly * regular + OvertimePay
print("The employee's total weekly pay is $" + str(TotalWeekPay))
