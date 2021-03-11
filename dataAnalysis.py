# Program to extract a particular row value
import xlrd
import math
from matplotlib import pyplot as plt

loc = ("data2.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)
pm2arr = []
pm10arr = []
pm2month = []
pm10month = []
pm2hrly = []
pm10hrly = []
i = 0
while(i < 24):
    pm2hrly = pm2hrly + [[]]
    pm10hrly = pm10hrly + [[]]
    i += 1
# p = [{(I HI  - I LO )/ (B HI - B LO )} * (C p -  B LO )]+I LO
lastMonth = 1
countDay = 0
sumPm2 = 0
sumPm10 = 0
for i in range(17, sheet.nrows):
    # print(sheet.row_values(i))
    a = sheet.row_values(i)
    pm2 = a[2]
    pm10 = a[3]
    if (pm2 != 'None'):
        # print(a[0])
        month = int(a[0].split(" ")[0].split("-")[1])
        hr = int(a[0].split(" ")[1].split(":")[0])
        # print(hr)
        pm2hrly[hr] = pm2hrly[hr]+[int(pm2)]

        if(lastMonth != month):
            pm2month += [sumPm2/countDay]
            sumPm2 = 0
            countDay = 0
            lastMonth = lastMonth+1
        countDay += 1
        sumPm2 += int(pm2)
        # print(pm2hrly)

pm2month += [sumPm2/countDay]
sumPm2 = 0
countDay = 0


i = 0
while(i < 24):
    pm2hrly[i] = sum(pm2hrly[i])/len(pm2hrly[i])
    i += 1


lastMonth = 1
countDay = 0
sumPm2 = 0
sumPm10 = 0
for i in range(17, sheet.nrows):
    # print(sheet.row_values(i))
    a = sheet.row_values(i)
    pm2 = a[2]
    pm10 = a[3]
    if (pm10 != 'None'):
        # print(a[0])
        month = int(a[0].split(" ")[0].split("-")[1])
        hr = int(a[0].split(" ")[1].split(":")[0])
        # print(hr)
        pm10hrly[hr] = pm10hrly[hr]+[int(pm10)]

        if(lastMonth != month):
            pm10month += [sumPm10/countDay]
            sumPm10 = 0
            countDay = 0
            lastMonth = lastMonth+1
        countDay += 1
        sumPm10 += int(pm10)
        # print(pm2hrly)

pm10month += [sumPm10/countDay]
sumPm2 = 0
countDay = 0


i = 0
while(i < 24):
    pm10hrly[i] = sum(pm10hrly[i])/len(pm10hrly[i])
    i += 1

dayhrs = [
    "00 AM",
    "01 AM",
    "02 AM",
    "03 AM",
    "04 AM",
    "05 AM",
    "06 AM",
    "07 AM",
    "08 AM",
    "09 AM",
    "10 AM",
    "11 AM",
    "12 PM",
    "01 PM",
    "02 PM",
    "03 PM",
    "04 PM",
    "05 PM",
    "06 PM",
    "07 PM",
    "08 PM",
    "09 PM",
    "10 PM",
    "11 PM"
]


monthNames = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
seasonName = ["Winter ", "Pre-monsoon ", "Monsoon ", "Post-monsoon"]
# print(len(pm2hrly), len(dayhrs))
plt.figure(figsize=(18, 8))
# plt.plot(dayhrs, pm2hrly, label="avg yearly pm2.5 concentrations hourly")
# plt.plot(monthNames, pm2month, label="monthly avg pm 2.5 concentrations ")
# plt.plot(seasonName, [((pm2month[11]+pm2month[0]+pm2month[1])/3), ((pm2month[2]+pm2month[3]+pm2month[4])/3), ((pm2month[5]+pm2month[6]+pm2month[7])/3), ((pm2month[8]+pm2month[9]+pm2month[10])/3)],
#          label="season wise avg pm 2.5 concentrations ")

# plt.plot(dayhrs, pm10hrly, label="avg yearly pm 10 concentrations hourly")
# plt.plot(monthNames, pm10month, label="monthly avg pm 10 concentrations ")
plt.plot(seasonName, [((pm10month[11]+pm10month[0]+pm10month[1])/3), ((pm10month[2]+pm10month[3]+pm10month[4])/3), ((pm10month[5]+pm10month[6]+pm10month[7])/3), ((pm10month[8]+pm10month[9]+pm10month[10])/3)],
         label="season wise avg pm 10 concentrations ")
# naming the x axis
plt.xlabel('Season of the year')
# naming the y axis
plt.ylabel('Season wise avg pm10 concentrations')
# giving a title to my graph
plt.title('')

# show a legend on the plot
plt.legend()
#plt.savefig('Season wise avg pm10 concentrations.jpg')

# function to show the plot
plt.show()
