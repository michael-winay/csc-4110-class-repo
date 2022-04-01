#Revision number 3-31-2022
##Begin Michael Winay here (3/31/2022)
print("Work Ticket 1:")
import math

#returns pi*r^2
def AreaofShape(**args):
    return (str(args["radius"] * args["radius"] * math.pi)+" cm^2")

circle = AreaofShape(radius = 5)
print(circle)
#Revision number 3-31-2022
##End Michael Winay here
#HALF-LIFE/ Ron Bass / John Richards Sr./ After-Burner Elite

print()

#Revision number 3-31-2022
##Begin Michael Winay here (3/31/2022)
print("Work Ticket 2:")

#returns cubed root
def VolumeofShape(**args):
    return (str('%.3f'%(args["volume"] ** (1. / 3)))+" cm^3")

cube = VolumeofShape(volume = 729)
print(cube)
#Revision number 3-31-2022
##End Michael Winay here
#HALF-LIFE/ Ron Bass / John Richards Sr./ After-Burner Elite

print()

#Revision number 3-31-2022
##Begin Michael Winay here (3/31/2022)
print("Work Ticket 3:")

#returns pythagorean theorum
def SideLengthofShape(**args):
    return (str('%.3f'%(math.sqrt(args["a"] * args["a"] + args["b"] * args["b"])))+" cm")

triangle = SideLengthofShape(a = 10, b = 18)
print(triangle)
#Revision number 3-31-2022
##End Michael Winay here
#HALF-LIFE/ Ron Bass / John Richards Sr./ After-Burner Elite

print()

#Revision number 3-31-2022
##Begin Michael Winay here (3/31/2022)
print("Work Ticket 4:")

#returns solution to the complex radical (no arguments needed)
def solveRadical(**args):
    return (math.sqrt( (math.pow((4.172 + 9.131844),3) - 18) / (-3.5 + (11.2 - 4.6) * math.pow((7 - 2.91683), -0.4)) ))

answer = solveRadical()
print(answer)
#Revision number 3-31-2022
##End Michael Winay here
#HALF-LIFE/ Ron Bass / John Richards Sr./ After-Burner Elite

print()

#Revision number 4-1-2022
##Begin Michael Winay here (4/1/2022)
print("Work Ticket 5:")

#Answers are explained in print statements
print()
print("Part One:")
print("Prediction: 1 2 5")

def f(a, b=4, c=5):
    print(a,b,c)
f(1, 2)

print("Since a and b are defined outside the function and c is not, the")
print("function will print the provided a and b and the predefined c")

print()
print("Part Two:")
print("Preiction: 1 2 3")

def f(a,b,c=5):
    print(a,b,c)
f(1,c=3,b=2)

print("Since a, b, and c are all defined outside the function, the")
print("predefined variables are effectively ignored")
#Revision number 4-1-2022
##End Michael Winay here
#HALF-LIFE/ Ron Bass / John Richards Sr./ After-Burner Elite
