#Revision number 3-23-2022
##Begin Michael Winay here (3/23/2022)
print("Work Ticket 1:")
import math

def sphere_volume(r):
    return (4*math.pi*radius)/3

#print should go here, since the function has a return value of the item being printed
radius = 5
print(sphere_volume(radius))
#Revision number 3-23-2022
##End Michael Winay here
#HALF-LIFE/ Ron Bass / John Richards Sr./ After-Burner Elite

print()

#Revision number 3-23-2022
##Begin Michael Winay here (3/23/2022)
print("Work Ticket 2:")

#flag determines the start and end range if the start is higher than the end
def print_range(start, end, flag):
    if(start <= end):
        flag = 1
        print(start, " ", end="")
        return(print_range(start + 1, end, flag))

    if(start > end and flag == 0):
        flag = 1
        return(print_range(end, start, flag))

start = 20
end = 1
flag = 0

print_range(start, end, flag)
print()
#Revision number 3-23-2022
##End Michael Winay here
#HALF-LIFE/ Ron Bass / John Richards Sr./ After-Burner Elite

print()

#Revision number 3-23-2022
##Begin Michael Winay here (3/23/2022)
print("Work Ticket 3:")

#basic euclidean algorithm
def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)

a = 18
b = 24

print("GCD of", a, "and", b, "is", gcd(a, b))
#Revision number 3-23-2022
##End Michael Winay here
#HALF-LIFE/ Ron Bass / John Richards Sr./ After-Burner Elite

print()

#Revision number 3-23-2022
##Begin Michael Winay here (3/23/2022)
import csv
import json

print("Work Ticket 4:")

sales_dict = {}

#open a csv reader and a json writer
try:
    with open('SalesJan2009.csv', mode='r') as input:
        reader = csv.reader(input)
        for rows in reader:
            key = rows[0]
            sales_dict[key] = rows

    with open('SalesJan2009.json', mode='w') as output:
        output.write(json.dumps(sales_dict, indent=4))

    print("Conversion Success")
except:
    print("Conversion failure")
#Revision number 3-23-2022
##End Michael Winay here
#HALF-LIFE/ Ron Bass / John Richards Sr./ After-Burner Elite