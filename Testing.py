
import csv
item = str("Plain Flour")
with open('itemData.csv', 'r') as file:
    for row in file:
        rowlist = row.split(',')
        if item == rowlist[0]:
            print(rowlist[2])
r1 = 1
r2 = 2
r3 = 0
r4 = 4

R = [r1, r2, r3, r4]
RN = ["r1", "r2", "r3", "r4"]
smallest_r = R.index(min(R))
print(f"R[{smallest_r}] = {RN[smallest_r]} = {R[smallest_r]}")
