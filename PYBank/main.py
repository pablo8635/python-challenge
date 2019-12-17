#Modules
import os
import csv
import statistics

pybank = os.path.join("PYBank.csv")

profit = []
accumulated=0
row_count = 0 
calculation = 0
revenue = 0
previous_r = 0 
average = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 99999999999]


with open (pybank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next (csvreader,None)

    for row in csvreader:
        profit.append(row[1])
        row_count = row_count +1

        #revenue
        revenue = int(row[1]) - previous_r
        previous_r = int(row[1])
        average.append(revenue)


        #Greatest Increase value
        if (revenue > greatestIncrease[1]):
            greatestIncrease[1] = revenue
            greatestIncrease[0] = row[0]

        if (revenue < greatestDecrease[1]):
            greatestDecrease[0] = row[0]
            greatestDecrease[1] = revenue

    for i in range (0, len(profit)):
        profit[i]=int(profit[i])

    
    for number in profit:
        accumulated = accumulated+int(number)
    
        

average_s = sum(average[1:len(average)]) / len(average)

#Print results
print(profit)
print (f'Total rows: {row_count}')
print (f'Total: ${accumulated}')
#print(average)
print(f"Average change: ${average_s}")
print(f"Greatest increase in Revenue: {greatestIncrease[0]} ${greatestIncrease[1]}")
print(f"Greatest decrease in Revenue: {greatestDecrease[0]} ${greatestDecrease[1]}")