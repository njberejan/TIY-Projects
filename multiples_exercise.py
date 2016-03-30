list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def multiple_of_3_or_5(list_of_numbers):

    multiples_of_3_or_5_list = []
    total = 0
    for number in list_of_numbers:
        if number % 3 == 0:
            multiples_of_3_or_5_list.append(number)
        elif number % 5 == 0:
            multiples_of_3_or_5_list.append(number)
        else:
            continue

    for number in multiples_of_3_or_5_list:
        #print(multiples_of_3_or_5_list)
        #print(total)
        total += number

    return total
    print(total)

multiple_of_3_or_5(list_of_numbers)
