list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def my_sum(list):
    total = 0
    for number in list:
      total = total + number

    return total

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
    print(multiples_of_3_or_5_list)
    # return my_sum(multiples_of_3_or_5_list)
    print(my_sum(multiples_of_3_or_5_list))


multiple_of_3_or_5(list_of_numbers)
