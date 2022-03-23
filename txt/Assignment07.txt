#Revision number 3-4-2022
##Begin Michael Winay here (3/4/2022)
print("Work Ticket 1:")
names = ['joe', 'tom', 'barb', 'sue', 'sally']
scores = [10, 23, 13, 18, 12]

scoreDict = {}
def makeDictionary(names, scores):
    merged = {}
    for n,s in zip(names,scores):
        merged.update({n:s})
    return merged

scoreDict = makeDictionary(names, scores)
print(scoreDict)
#Revision number 3-4-2022
##End Michael Winay here
#Zion Worship Cult/ Ram Vuduku / Rich Eissen/ the Zion Project

print()

#Revision number 3-4-2022
##Begin Michael Winay here (3/4/2022)
print("Work Ticket 2:")
ticket_two_char_continue = 'y'
while(ticket_two_char_continue == 'y'):
    ticket_two_string_search = input("Enter name to find score for: ")
    print(scoreDict.get(ticket_two_string_search))
    ticket_two_char_continue = input("Find another (y/n)?: ")
#Revision number 3-4-2022
##End Michael Winay here
#Zion Worship Cult/ Ram Vuduku / Rich Eissen/ the Zion Project

print()

#Revision number 3-4-2022
##Begin Michael Winay here (3/4/2022)
print("Work Ticket 3:")
ticket_three_char_continue = 'y'
while(ticket_three_char_continue == 'y'):
    ticket_three_string_name = input("Enter name to add: ")
    ticket_three_int_score = input("Enter their score: ")
    scoreDict.update({ticket_three_string_name:ticket_three_int_score})
    ticket_three_char_continue = input("Add another (y/n)?: ")

print(scoreDict)
#Revision number 3-4-2022
##End Michael Winay here
#Zion Worship Cult/ Ram Vuduku / Rich Eissen/ the Zion Project

print()

#Revision number 3-4-2022
##Begin Michael Winay here (3/4/2022)
print("Work Ticket 4:")
sortedScoreDict = {}
for s in sorted(scoreDict):
    sortedScoreDict[s] = scoreDict[s]

print(sortedScoreDict)
#Revision number 3-4-2022
##End Michael Winay here
#Zion Worship Cult/ Ram Vuduku / Rich Eissen/ the Zion Project

print()

#Revision number 3-4-2022
##Begin Michael Winay here (3/4/2022)
print("Work Ticket 5:")
ticket_five_char_continue = 'y'
ticket_five_char_option = ''
while(ticket_five_char_continue != 'x'):
    ticket_five_char_option = input("Enter operation ((a)dd, (d)elete, (q)uery, (p)rint, e(x)it: ")
    if(ticket_five_char_option == 'a'):
        ticket_five_string_name_add = input("Enter name to add: ")
        ticket_five_int_score_add = input("Enter their score: ")
        scoreDict.update({ticket_five_string_name_add:ticket_five_int_score_add})
    elif(ticket_five_char_option == 'd'):
        ticket_five_string_name_del = input("Enter name to remove: ")
        del scoreDict[ticket_five_string_name_del]
    elif(ticket_five_char_option == 'q'):
        ticket_five_string_search = input("Enter name to find score for: ")
        print(scoreDict.get(ticket_five_string_search))
    elif(ticket_five_char_option == 'p'):
        print(scoreDict)
    elif(ticket_five_char_option == 'x'):
        break
    else:
        print("Invalid option!")
        ticket_five_char_continue = 'y'
#Revision number 3-4-2022
##End Michael Winay here
#Zion Worship Cult/ Ram Vuduku / Rich Eissen/ the Zion Project