import grossSalary as gs
import salaryDeduction as sd
import netSalary as ns


print(str.title("employee information"))
name = str(input("Employee Name: "))
hour = int(input("Number of Hours: "))
SSS = float(input("SSS: "))
Philhealth = float(input("Philhealth: "))
otherLoan = float(input("Housing Loan: "))
"""hello"""
RatePerHour = 500
grossSalary = gs.gross(hour, RatePerHour)
tax = grossSalary * 0.12
totalDeductions = sd.salaryDeduction(SSS, Philhealth, otherLoan, tax)
netSalary = ns.netSalary(grossSalary, totalDeductions)

print("\nTotal Deduction \nGross Salary: " + str(grossSalary))
print("Total Deductions: " + str(totalDeductions))
print("Tax : "+ str(tax))
print("Net Salary : " + str(netSalary))
