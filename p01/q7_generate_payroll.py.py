
# coding: utf-8

# In[ ]:


name = input("Enter name: ")
hours = int(input("Enter number of hours worked weekly: "))
pay = float(input("Enter hourly pay rate: "))
cpf = float(input("Enter CPF contribution rate(%): "))

gross_pay = pay*hours
cpf_money = (cpf/100)*gross_pay

print("Payroll statement for {}".format(name))
print("Number of hours worked in week: {}".format(hours))
print("Hourly pay rate: {}".format(pay))
print("Gross pay = ${0:.2f}".format(gross_pay))
print("CPF contribution at {0}% = ${1:.2f}".format(cpf,cpf_money))
print("Net pay = ${0:.2f}".format(gross_pay - cpf_money))

