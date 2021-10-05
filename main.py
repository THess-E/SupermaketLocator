import csv
import math
#SETUP
complete = bool(0)
itemfound = bool(0)
contact = bool(0)
x1 = int(input("What is your Xposition"))
y1 = int(input("What is your Yposition"))
item = str(input("What item are you looking for"))
#two weeks of work to get All of the infomation about an item
with open('itemData.csv', 'r') as file:
    for row in file:
        rowlist = row.split(',')
        if item == rowlist[0]:
           x2 = int(rowlist[2])
           y2 = int(rowlist[3])
           #itemcount = int(rowlist[1])
           itemfound = bool(1)
    if not itemfound:
        print("Item not found")

#getting some basic maths to use for caluating graphs

xdif = x2-x1
ydif = y2-y1 #The
grad = ydif/xdif # the gradient of the line between the user and the item
yint = y1 - grad*x1 # The Y intercept of the line might not need
midpointX = (x1+x2)/2 # The midpoint of the item and user as two vairables
midpointY = (y1+y2)/2
dist = math.sqrt((x2-x1)**2 + (y2-y1)**2) #Distance between User and item
# Defining All funtions
def checkColisons():
    if 7>(1 * grad + yint) > 1:
        contact = bool(1)
    elif 7>(3 * grad + yint) > 1:
        contact = bool(1)
    elif 7>(4 * grad + yint) > 1:
        contact = bool(1)
    elif 7>(5 * grad + yint) > 1:
        contact = bool(1)
    elif 7>(6 * grad + yint) > 1:
        contact = bool(1)
    elif 7>(7 * grad + yint) > 1:
        contact = bool(1)
    elif 7>(8 * grad + yint) > 1:
        contact = bool(1)
    elif 7>(9 * grad + yint) > 2:
        contact = bool(1)
    elif 7>(10 * grad + yint) > 2:
        contact = bool(1)
    elif 9>(11 * grad + yint) > 2:
        contact = bool(1)
    elif 9>(12 * grad + yint) > 2:
        contact = bool(1)
    elif 9>(13 * grad + yint) > 2:
        contact = bool(1)
    elif 9>(14 * grad + yint) > 2:
        contact = bool(1)
    elif 9>(15 * grad + yint) > 2:
        contact = bool(1)
    elif 9>(16 * grad + yint) > 2:
        contact = bool(1)
    elif 9>(17 * grad + yint) > 2:
        contact = bool(1)
def findClosestRP():
    r1 = math.sqrt((0.5-midpointX)**2 + (0.5-midpointY)**2)
    r2 = math.sqrt((1.5-midpointX)**2 + (0.5-midpointY)**2)
    r3 = math.sqrt((2.5-midpointX)**2 + (0.5-midpointY)**2)
    r4 = math.sqrt((3.5-midpointX)**2 + (0.5-midpointY)**2)
    r5 = math.sqrt((4.5-midpointX)**2 + (0.5-midpointY)**2)
    r6 = math.sqrt((5.5-midpointX)**2 + (0.5-midpointY)**2)
    r7 = math.sqrt((6.5-midpointX)**2 + (0.5-midpointY)**2)
    r8 = math.sqrt((7.5-midpointX)**2 + (0.5-midpointY)**2)
    r9 = math.sqrt((8.5-midpointX)**2 + (0.5-midpointY)**2)
    r10 = math.sqrt((8.5-midpointX)**2 + (1.5-midpointY)**2)
    r11 = math.sqrt((9.5-midpointX)**2 + (1.5-midpointY)**2)
    r12 = math.sqrt((10.5-midpointX)**2 + (1.5-midpointY)**2)
    r13 = math.sqrt((11.5-midpointX)**2 + (1.5-midpointY)**2)
    r14 = math.sqrt((12.5-midpointX)**2 + (1.5-midpointY)**2)
    r15 = math.sqrt((13.5-midpointX)**2 + (1.5-midpointY)**2)
    r16 = math.sqrt((14.5-midpointX)**2 + (1.5-midpointY)**2)
    r17 = math.sqrt((15.5-midpointX)**2 + (1.5-midpointY)**2)
    r18 = math.sqrt((16.5-midpointX)**2 + (1.5-midpointY)**2)
    r19 = math.sqrt((17.5-midpointX)**2 + (1.5-midpointY)**2)
    #bottom
    r20 = math.sqrt((0.5-midpointX)**2 + (7.5-midpointY)**2)
    r21 = math.sqrt((1.5-midpointX)**2 + (7.5-midpointY)**2)
    r22 = math.sqrt((2.5-midpointX)**2 + (7.5-midpointY)**2)
    r23 = math.sqrt((3.5-midpointX)**2 + (7.5-midpointY)**2)
    r24 = math.sqrt((4.5-midpointX)**2 + (7.5-midpointY)**2)
    r25 = math.sqrt((5.5-midpointX)**2 + (7.5-midpointY)**2)
    r26 = math.sqrt((6.5-midpointX)**2 + (7.5-midpointY)**2)
    r27 = math.sqrt((7.5-midpointX)**2 + (7.5-midpointY)**2)
    r28 = math.sqrt((8.5-midpointX)**2 + (7.5-midpointY)**2)
    r29 = math.sqrt((9.5-midpointX)**2 + (7.5-midpointY)**2)
    r30 = math.sqrt((10.5-midpointX)**2 + (7.5-midpointY)**2)
    r31 = math.sqrt((10.5-midpointX)**2 + (9.5-midpointY)**2)
    r32 = math.sqrt((11.5-midpointX)**2 + (9.5-midpointY)**2)
    r33 = math.sqrt((12.5-midpointX)**2 + (9.5-midpointY)**2)
    r34 = math.sqrt((13.5-midpointX)**2 + (9.5-midpointY)**2)
    r35 = math.sqrt((14.5-midpointX)**2 + (9.5-midpointY)**2)
    r36 = math.sqrt((15.5-midpointX)**2 + (9.5-midpointY)**2)
    r37 = math.sqrt((16.5-midpointX)**2 + (9.5-midpointY)**2)
    r38 = math.sqrt((17.5-midpointX)**2 + (9.5-midpointY)**2)
#checking if the line colides with any alises
while not(complete):
    checkColisons()
    if contact:
        findClosestRP()
#for debugging and devolopment
print("Y Intercept = " + str(yint))
print("Gradient = " + str(grad))
print("y="+str(grad)+"x+"+str(yint))
print("X of midpoint = " + str(midpointX))
print("Y of midpoint = " + str(midpointY))
