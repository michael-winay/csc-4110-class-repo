#Part 1
main_list = [1121, "Jackie Grainger", 22.22,\
 1122, "Jignesh Thrakkar", 25.25,\
 1127, "Dion Green", 28.75, False,\
 24.32, 1132, "Jacob Gerber",\
 "Sarah Sanderson", 23.45, 1137, True,\
 "Brandon Heck", 1138, 25.84, True,\
 1152, "David Toma", 22.65,\
 23.75, 1157, "Charles King", False,\
 "Jackie Grainger", 1121, 22.22, False,\
 22.65, 1152, "David Toma"]

#Parses arguments into key-pair value based on type
def parse_line(*args):
    parse_type = [args[0], args[1], args[2]]
    parsed_list = [0, "", 0.0]
    parsed_key = {}
    for i in range(3):
        if(type(parse_type[i]) == int):
            parsed_list[0] = parse_type[i]
        elif(type(parse_type[i]) == str):
            parsed_list[1] = parse_type[i]
        else:
            parsed_list[2] = parse_type[i]
    try:
        parsed_key[parsed_list[0]] = [parsed_list[1], parsed_list[2], args[3]]
    except:
        parsed_key[parsed_list[0]] = [parsed_list[1], parsed_list[2]]

    return parsed_key

#converts list to dictionary (works in tandem with parse_line)
def convert(l):
    converted={}
    i = 0
    while i < len(l):
        check_ahead = False
        try:
            check_ahead = type(l[i + 3])
        except:
            check_ahead = False
        if(check_ahead == type(True)):
            converted.update(parse_line(l[i], l[i + 1], l[i + 2], l[i + 3]))
            i += 4
        else:
            converted.update(parse_line(l[i], l[i + 1], l[i + 2]))
            i += 3
    return converted

#Part 2, 3
main_dict = convert(main_list)
main_dict_sorted = {}

#sorts dictionary
for i in sorted(main_dict):
    main_dict_sorted[i] = main_dict[i]

underpaid_salaries = []
company_raises = {}

#Part 4, 5, 6
for i in main_dict_sorted:
    main_dict_sorted[i].append(main_dict_sorted[i][1] * 1.3)
    if(main_dict_sorted[i][-1] > 28.15 and main_dict_sorted[i][-1] < 30.65):
        underpaid_salaries.append(main_dict_sorted[i])

    if(main_dict_sorted[i][1] > 22 and main_dict_sorted[i][1] < 24):
        company_raises[main_dict_sorted[i][0]] = main_dict_sorted[i][1] * 1.05
    elif(main_dict_sorted[i][1] > 24 and main_dict_sorted[i][1] < 26):
        company_raises[main_dict_sorted[i][0]] = main_dict_sorted[i][1] * 1.04
    elif(main_dict_sorted[i][1] > 26 and main_dict_sorted[i][1] < 28):
        company_raises[main_dict_sorted[i][0]] = main_dict_sorted[i][1] * 1.03
    else:
        company_raises[main_dict_sorted[i][0]] = main_dict_sorted[i][1] * 1.02

#Part 7
print("Sorted dictionary:", main_dict_sorted, "\n")
print("Underpaid salaries:", underpaid_salaries, "\n")
print("Company raises:", company_raises, "\n")