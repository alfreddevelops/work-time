# importing excel sheet
from openpyxl import Workbook
from openpyxl.formula.translate import Translator

workbook = Workbook()
work_time = workbook.active

work_time['A1'] = "Date"
work_time['B1'] = "Hours"
work_time['C1'] = "Outlet"
work_time['D1'] = "Per Hour"
work_time['E1'] = "Earning $"

# DATES
work_time['A2'] = "9 dec"
work_time['A3'] = "10 dec"

# HOURS
work_time['B2'] = "10"
work_time['B3'] = "10"
#print (work_time['B2'].value)

# PER HOUR
work_time['C2'] = "SMU"
work_time['C3'] = "MBS"
# print(work_time['C3'].value)

# OUTLETS
work_time['D2'] = 8
work_time['D3'] = 10
# print(mbs.value)

# EARNING USING OPERATIONS
work_time['E2'].value = float(
    work_time['B2'].value) * float(work_time['D2'].value)
work_time['E3'].value = float(
    work_time['B3'].value) * float(work_time['D3'].value)

total = work_time['E4']
total.value = float(work_time['E2'].value) + float(work_time['E3'].value)
def calculate_cpf(total):
    if int(total.value) > 500:
        #overwriting old total value with new value after cpf
        total.value = int(total.value) * 80/100
        print("more than 500")
        #print new value after cpf
        print(total.value)
    else:
        print("less than 500")

# CONVERTING CELL VALUE INTO FLOAT AND FINDING VALUE OF EARNING
#work_time['D2'] = float(work_time['B2'].value) * 10
# if work_time['D2':'D3'].value == "MBS":
#    work_time['E2'] = float(work_time['B2'].value) * 10
# else:
#    work_time['D2'] = float(work_time['B2'].value) * 8

# FOR LOOP TO CYCLE THROUGH THE HOURS COLUMNS AND PAY COLUMNS
# USING VAR
# def calculate_pay():
#     i = 2
#     for i in range (work_time['B'].rows):
#         print (work_time['B' + 'i'].value)


workbook.save("worktime.xlsx")
