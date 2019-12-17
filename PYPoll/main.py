#Import modules
import os
import csv

#Variables
votes = 0
candidates = []
votesc_1 = 0
votesc_2 = 0
votesc_3 = 0
votesc_4 = 0 

#CSV
pypoll = os.path.join("PYPoll.csv")


with open (pypoll, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next (csvreader,None)

    for row in csvreader:
        votes = votes + 1
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == candidates[0]:
            votesc_1 = votesc_1 + 1
        elif row[2] == candidates[1]:
            votesc_2 = votesc_2 + 1
        elif row[2] == candidates[2]:
            votesc_3 = votesc_3 + 1
        elif row[2] == candidates [3]:
            votesc_4 = votesc_4 + 1

output = (f'Total votes = {votes}\n'
            f'{candidates[0]}: {votesc_1/votes} {votesc_1}\n'
            f'{candidates[1]}: {votesc_2/votes} {votesc_2}\n'
            f'{candidates[2]}: {votesc_3/votes} {votesc_3}\n'
            f'{candidates[3]}: {votesc_4/votes} {votesc_4}\n'
            f'The winner is {candidates[0]}'
) 

print(output)