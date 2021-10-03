import csv
item = str("Plain Flour")
with open('itemData.csv', 'r') as file:
    for row in file:
        rowlist = row.split(',')
        if item == rowlist[0]:
            print(rowlist[2])

