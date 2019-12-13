#importing excel sheet
from openpyxl import Workbook

workbook = Workbook()
work_time = workbook.active

work_time['A1'] = "Date"
work_time['B1'] = "Hours"
work_time['C1'] = "Outlet"
work_time['D1'] = "Earning"

#DATES
work_time['A2'] = "9 dec"
work_time['A3'] = "10 dec"

#HOURS
work_time['B2'] = "10"
work_time['B3'] = "10"

#OUTLETS
work_time['C2'].value = "MBS"
work_time['C3'].value = "MBS"
tuple(work_time['C'].value)

#CONVERTING CELL VALUE INTO FLOAT AND FINDING VALUE OF EARNING
#work_time['D2'] = float(work_time['B2'].value) * 10
if work_time['C'].value == "MBS":
    work_time['D2'] = work_time['B2'].value * 10
else:
    work_time['D2'] = work_time['B2'].value * 8


workbook.save("worktime.xlsx")
