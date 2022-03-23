#Revision number 2-17-2022
##Begin Michael Winay here (2/15/2022)
print("Work Ticket One:")

#Begin step 1
last_name = "winay"

#Begin step 2
first_name = "MICHAEL"

#Begin step 3
print("Hello,", first_name.lower(), last_name.upper())

#Begin step 4
#An extra newline is added from print()
print("\n")

#Begin step 5
full_name = "Michael Winay"

#Begin step 6
print(full_name[:full_name.index(" ") + 1])

#Begin step 7
full_name = full_name + ", Walsh College Student"
print(full_name)

#Begin step 8
#Windows CMD does not support italics.
print("\"Start by doing what\'s necessary; then do\nwhat\'s possible; and suddenly you are doing\nthe impossible - Francis of Assisi\"")

#Begin step 9
decimal_one = 7.865
decimal_two = 8.947

#Begin step 10
decimal_add = decimal_one + decimal_two
decimal_subtract = decimal_one - decimal_two
decimal_multiply = decimal_one * decimal_two
decimal_divide = decimal_one / decimal_two

#Begin step 11
#printing via multiple print arguments (no formatting)
print(decimal_one, "+", decimal_two, "=", decimal_add)
#printing via concatenation (no formatting)
print(str(decimal_one) + " - " + str(decimal_two) + " = " + str(decimal_subtract))
#printing via formatted placeholder
print("%1.1f * %1.1f = %1.1f" %(decimal_one, decimal_two, decimal_multiply))
#printing via fstring
print(f'{decimal_one:.2f} / {decimal_two:.2f} = {decimal_divide:.3f}')

#Begin step 12
import math 
sq_root = round(math.sqrt(decimal_multiply), 2)
print("sqrt(",decimal_multiply,") =", sq_root)

#Begin step 13
import datetime

current_month = datetime.date.today().strftime("%B")
current_day = datetime.datetime.today().day

#Begin step 14
print("Today is day " + str(current_day) + " of the month of " + current_month)

#Revision number 2-17-2022
##End Michael Winay here
#the Omega - Cypress International Equity Division/ Ram Fujitsu / Rich Alderman/ grant $3700
