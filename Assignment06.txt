#Revision number 2-25-2022
##Begin Michael Winay here (2/25/2022)
print("Work Ticket 1:")
print("This string has \"double quotation marks\" in it")

print()

print("This strings\' an apostrophe in it")
print("""
String         spans
            multiple
lines           with whitespace preserved
""")
print("This string is formed", end=" ")
print("by multiple statements")
#Revision number 2-25-2022
##End Michael Winay here
#Zion Worship Cult/ Ram Vuduku / Rich Eissen/ the Zion Project

print()

#Revision number 2-25-2022
##Begin Michael Winay here (2/25/2022)
print("Work Ticket 2:")
ticket_two_string = "String is thirty eight characters long"
print(ticket_two_string)
print("Length of above string is:", len(ticket_two_string))

print()

ticket_two_string_concat_one = "First part of the concat"
ticket_two_string_concat_two = "second part of the concat"

print(ticket_two_string_concat_one)
print(ticket_two_string_concat_two)
print(ticket_two_string_concat_one + ticket_two_string_concat_two)

print()
print(ticket_two_string_concat_one)
print(ticket_two_string_concat_two)
print(ticket_two_string_concat_one + " " + ticket_two_string_concat_two)

print()

ticket_two_string_bazinga = "bazinga"
print("normal:", ticket_two_string_bazinga)
print("sliced:", ticket_two_string_bazinga[2:6])
#Revision number 2-25-2022
##End Michael Winay here
#Zion Worship Cult/ Ram Vuduku / Rich Eissen/ the Zion Project

print()

#Revision number 2-25-2022
##Begin Michael Winay here (2/25/2022)
print("Work Ticket 3:")
ticket_three_string_animal_one = "Animals"
ticket_three_string_animal_two = "Badger"
ticket_three_string_animal_three = "Honey Bee"
ticket_three_string_animal_four = "Honey Badger"

print("Before:")
print(ticket_three_string_animal_one)
print(ticket_three_string_animal_two)
print(ticket_three_string_animal_three)
print(ticket_three_string_animal_four)

ticket_three_string_animal_one = ticket_three_string_animal_one.lower()
ticket_three_string_animal_two = ticket_three_string_animal_two.lower()
ticket_three_string_animal_three = ticket_three_string_animal_three.lower()
ticket_three_string_animal_four = ticket_three_string_animal_four.lower()

print("After:")
print(ticket_three_string_animal_one)
print(ticket_three_string_animal_two)
print(ticket_three_string_animal_three)
print(ticket_three_string_animal_four)

print()

ticket_three_string_animal_one_ptwo = "Animals"
ticket_three_string_animal_two_ptwo = "Badger"
ticket_three_string_animal_three_ptwo = "Honey Bee"
ticket_three_string_animal_four_ptwo = "Honey Badger"

print("Before:")
print(ticket_three_string_animal_one_ptwo)
print(ticket_three_string_animal_two_ptwo)
print(ticket_three_string_animal_three_ptwo)
print(ticket_three_string_animal_four_ptwo)

ticket_three_string_animal_one_ptwo = ticket_three_string_animal_one_ptwo.upper()
ticket_three_string_animal_two_ptwo = ticket_three_string_animal_two_ptwo.upper()
ticket_three_string_animal_three_ptwo = ticket_three_string_animal_three_ptwo.upper()
ticket_three_string_animal_four_ptwo = ticket_three_string_animal_four_ptwo.upper()

print("After:")
print(ticket_three_string_animal_one_ptwo)
print(ticket_three_string_animal_two_ptwo)
print(ticket_three_string_animal_three_ptwo)
print(ticket_three_string_animal_four_ptwo)

print()

ticket_three_string_food_one = " Filet Mignon"
ticket_three_string_food_two = "Brisket "
ticket_three_string_food_three = " Cheeseburger "

print("Before:")
print(ticket_three_string_food_one)
print(ticket_three_string_food_two)
print(ticket_three_string_food_three)

ticket_three_string_food_one = ticket_three_string_food_one.strip()
ticket_three_string_food_two = ticket_three_string_food_two.strip()
ticket_three_string_food_three = ticket_three_string_food_three.strip()

print("After:")
print(ticket_three_string_food_one)
print(ticket_three_string_food_two)
print(ticket_three_string_food_three)

print()

ticket_three_string_be_one = "Becomes"
ticket_three_string_be_two = "becomes"
ticket_three_string_be_three = "BEAR"
ticket_three_string_be_four = "bEautiful"

print(ticket_three_string_be_one, ":", ticket_three_string_be_one.startswith("be"))
print(ticket_three_string_be_two, ":", ticket_three_string_be_two.startswith("be"))
print(ticket_three_string_be_three, ":", ticket_three_string_be_three.startswith("be"))
print(ticket_three_string_be_four, ":", ticket_three_string_be_four.startswith("be"))
#Revision number 2-25-2022
##End Michael Winay here
#Zion Worship Cult/ Ram Vuduku / Rich Eissen/ the Zion Project

print()

#Revision number 2-25-2022
##Begin Michael Winay here (2/25/2022)
print("Work Ticket 4:")
ticket_four_string_intcast = "350"
print("My number: " + ticket_four_string_intcast)
ticket_four_string_intcast = int(ticket_four_string_intcast)
print("Number multiplied by 10:", ticket_four_string_intcast * 10)

print()

ticket_four_string_floatcast = "350.0"
print("My number: " + ticket_four_string_floatcast)
ticket_four_string_floatcast = float(ticket_four_string_floatcast)
print("Number multiplied by 10:", ticket_four_string_floatcast * 10)

print()
ticket_four_string_strobj = "Michael"
ticket_four_string_intobj = 5
print(ticket_four_string_strobj, str(ticket_four_string_intobj))

print()

print("Please enter two numbers")
ticket_four_float_one = input()
ticket_four_float_two = input()

try:
    print("The product of", ticket_four_float_one, "and", ticket_four_float_two, "is", float(ticket_four_float_one) * float(ticket_four_float_two))
except:
    print("Invalid input detected")

print()

ticket_four_string_find = "Hello, can you find me?"
print("String:", ticket_four_string_find)
print("Location of target \"find\":", ticket_four_string_find.find("find"))
#Revision number 2-25-2022
##End Michael Winay here
#Zion Worship Cult/ Ram Vuduku / Rich Eissen/ the Zion Project