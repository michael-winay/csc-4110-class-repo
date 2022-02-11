#Revision number 2-1-2022
##Begin Michael Winay here (2/1/2022)
print("Issue One:")
value_issue_one = int(input("Enter a number: "))
#Added parentheses to make sure operations are done in order
value_issue_one = int(((((value_issue_one + 2) * 3) - 6) / 3))
print("Here is the output:", value_issue_one)
#Revision number 2-1-2022
##End Michael Winay here
#Omega Group/ Ram Valud / Michael Walker/  project greenwood321

#Revision number 2-2-2022
##Begin Michael Winay here (2/2/2022)
#Just a copy/paste job for the first two groups
print()
print("Issue Two:")
print("Group 1:")
my_var1 = 7.0 
my_var2 = 5 
print(my_var1 % my_var2)

print("Group 2:")
x = 4 
y = 5 
print(x//y)

print("Group 3:")
value2 = 30-3**2+8//3**2*10
#I added an output section here. It was not necessairly in the instructions,
#but it is beneficial to actually see the result of this operation
print("output:", value2)
#Revision number 2-2-2022
##End Michael Winay here
#Omega Group/ Ram Valud / Michael Walker/  project greenwood321

#Revision number 2-2-2022
##Begin Michael Winay here (2/2/2022)
print()
print("Issue Three:")
#This code is driver code to test type casting. It can be uncommented in order to perform testing
#value_issue_three = input("Enter a number: ")
#will_continue = True
#while will_continue:
#    print("Input as string:", str(value_issue_three))
#    print("Input as integer:", int(value_issue_three))
#    print("Input as float:", float(value_issue_three))
#    print("Continue? y/n")
#    log_continue = input()
#    will_continue = True if log_continue == y or log_continue == Y else False
print("Can uncomment source code to enable testing")
print("Findings:")
print("Cannot receieve any input containing alphabet or special characters.") 
print("They cannot be cast as integers, at least not with basic casting")
#Revision number 2-2-2022
##End Michael Winay here
#Omega Group/ Ram Valud / Michael Walker/  project greenwood321

#Revision number 2-3-2022
##Begin Michael Winay here (2/3/2022)
print()
print("Issue Four:")
#Straightforward copy paste
value_issue_four = 2**2**3
print("a)", value_issue_four)
value_issue_four = 2**(2**3)
print("b)", value_issue_four)
value_issue_four = (2**2)**3
print("c)", value_issue_four)
#Additional output explaining the difference
print("Value \"c\" has a different value")
#Revision number 2-3-2022
##End Michael Winay here
#Omega Group/ Ram Valud / Michael Walker/  project greenwood321

#Revision number 2-3-2022
##Begin Michael Winay here (2/3/2022)
import random

print()
print("Issue Five: The Pirate One")
print("The Rules:")
print("-Buy in is one gold")
print("-six or higher is a win")
print("-Wagering odds are therefore 50%")
print("How much gold do you have?")
hoard = int(input())
#Will loop as long as you have a gold count higher than 0. It will draw a new number every iteration
while(hoard > 0):
    print("Your Gold:", hoard)
    print("What's yer wager?")
    wager = int(input())
    spin = random.randint(1, 10)
    if(spin > 5):
        print("The number drawn was a", spin, ". You win this time...")
        hoard += wager
    else:
        print("The number drawn was a", spin, ". You lose...")
        hoard -= wager
print("You don't have any gold left...")
#Revision number 2-3-2022
##End Michael Winay here
#Omega Group/ Ram Valud / Michael Walker/  project greenwood321

#Revision number 2-3-2022
##Begin Michael Winay here (2/3/2022)
print()
print("Issue Six:")
#Every word in English has a vowel or the letter 'Y'. If they are removed from the pool of characters,
#there will be no words possible. 
print("Password list:")
for i in range(40):
    password = ''
    #This part generates the non-vowel characters one after the other up to 24 times
    for j in range(random.randint(10,24)):
        vowel = True
        while(vowel):
            random_char = random.randint(97, 122)
            if (random_char != 97 and random_char != 101 and random_char != 105 and random_char != 111 and random_char != 117 and random_char != 121):
                vowel = False
            else:
                vowel = True
        password += chr(random_char)

    #This part generates up to 7 special characters to insert randomly into the password
    for j in range(random.randint(3,7)):
        random_spcl = chr(random.randint(33, 38))
        random_pos = random.randint(1,len(password))
        password = password[:random_pos] + random_spcl + password[random_pos:]
    
    print(password)
#Revision number 2-3-2022
##End Michael Winay here
#Omega Group/ Ram Valud / Michael Walker/  project greenwood321