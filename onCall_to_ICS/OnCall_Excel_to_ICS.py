# for call
from ics import Calendar, Event

#for excel
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

date_col = 1
on_call_col = 1
second_on_call_col = 

# Give the location of the file
onCallFile = ("path of file")

# To open Workbook
wb = load_workbook(filename = onCallFile)
ws1 = wb.active

# For row 0 and column 0
print(ws1['A1'])

On_call_drs = []
Second_on_call_drs = []



On_call_drs.append(sheet.cell_value(0,on_call_col))
Second_on_call_drs.append(sheet.cell_value(0,second_on_call_col))


ali_calendar = Calendar()
e = Event()
e.name = "Ali on call"
e.begin = '2014-01-01 00:00:00'
e.all_day = True
ali_calendar.events.add(e)
ali_calendar.events




with open('ali.ics', 'w') as f:
    f.writelines(ali_calendar.serialize_iter())

