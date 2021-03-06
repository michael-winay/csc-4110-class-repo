#Revision number 2-8-2022
##Begin Michael Winay here (2/8/2022)
print("Work Ticket 1:")
print("Please enter a string:")
work_one_str = input()
print("You entered", work_one_str, "and its type is <class \'str\'>")
print("Please enter an integer:")
#This is, in fact, what was requested on the ticket
work_one_int = input()
print("You entered", work_one_int, "and its type is <class \'str\'>")
#Revision number 2-8-2022
##End Michael Winay here
#Omega Group/ Ram Valud / Michael Walker/  project greenwood321

print()

#Revision number 2-8-2022
##Begin Michael Winay here (2/8/2022)
#Provided tabs show up in the client terminal, this will produce the right result
print("Work Ticket 2:")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print()
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are")
#Revision number 2-8-2022
##End Michael Winay here
#Omega Group/ Ram Valud / Michael Walker/  project greenwood321

print()

#Revision number 2-8-2022
##Begin Michael Winay here (2/8/2022)
#Pi was extrapolated out to 20 digits to avoid importing the Math library
print("Work Ticket 3:")
pi = 3.1415926535897932385
print("Please enter radius:")
radius = float(input())
area = pi * (radius * radius)
print("r =", radius)
print("Area =", area)
#Revision number 2-8-2022
##End Michael Winay here
#Omega Group/ Ram Valud / Michael Walker/  project greenwood321

print()

#Revision number 2-8-2022
##Begin Michael Winay here (2/8/2022)
print("Work Ticket 4:")
print("Please input letter:")
work_four_char = input()
#letter converted to lower for checking purposes. uppercase version is stored in the original if needed
work_four_char_adjust = work_four_char.lower()
#y was not included in vowel checking
if(work_four_char_adjust == 'a' or work_four_char_adjust == 'e' or work_four_char_adjust == 'i' or work_four_char_adjust == 'o' or work_four_char_adjust == 'u'):
    print("Your input,", work_four_char, ", was a vowel")
else:
    print("Your input,", work_four_char, ", was not a vowel")
#Revision number 2-8-2022
##End Michael Winay here
#Omega Group/ Ram Valud / Michael Walker/  project greenwood321

print()

#Revision number 2-9-2022
##Begin Michael Winay here (2/9/2022)
print("Work Ticket 5:", [x*x*x*x for x in range(20)])
#Revision number 2-9-2022
##End Michael Winay here
#Omega Group/ Ram Valud / Michael Walker/  project greenwood321

print()

#Revision number 2-9-2022
##Begin Michael Winay here (2/9/2022)
import random

print("Work Ticket 6:")
#red and black numbers are stored in separate lists. if a zero index is drawn, then it is converted to the appropriate green later
red = [0, 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [0, 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
log = []
user_choice_six = True

while(user_choice_six == True):
    #first the color is selected, then the number
    red_black = random.randint(1, 2)
    number = random.randint(0, 18)

    if(red_black == 1):
        if(number == 0):
            print("GREEN 0")
            log.append("GREEN 0")
            print()
        else:
            print("RED", red[number])
            log.append("RED "+str(red[number]))
            print()

    else:
        if(number == 0):
            print("GREEN 00")
            log.append("GREEN 00")
            print()
        else:
            print("BLACK", black[number])
            log.append("BLACK "+str(black[number]))
            print()

    print("Log so far:")
    for i in log:
        print(i)
    print()
    print("Choose another number (y/n)?")
    user_choice_six = True if input() == "y" else False
#Revision number 2-9-2022
##End Michael Winay here
#Omega Group/ Ram Valud / Michael Walker/  project greenwood321

print()

#Revision number 2-10-2022
##Begin Michael Winay here (2/10/2022)
print("Work Ticket 7:")
DinnerGuests = []
DateInvited = []
user_choice_seven = True

#this works very similarly to ticket six
while(user_choice_seven == True):
    print("Enter guest's name:")
    work_seven_name = str(input())
    print("Enter date that", work_seven_name, "was invited (mm-dd-yyyy):")
    work_seven_date = str(input())

    DinnerGuests.append(work_seven_name)
    DateInvited.append(work_seven_date)

    if(len(work_seven_name) > 15):
        print(work_seven_name, "goes on a long tag")
    else:
        print(work_seven_name, "goes on a short tag")

    print()
    print("Enter another name (y/n)?")
    user_choice_seven = True if input() == "y" else False

print()
print("Your guest list is")
#One line, as requested
print([DinnerGuests[i]+":"+DateInvited[i] for i in range(len(DinnerGuests))])
#Revision number 2-10-2022
##End Michael Winay here
#Omega Group/ Ram Valud / Michael Walker/  project greenwood321
