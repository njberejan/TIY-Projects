import statistics
def user_statistics():

    total_inputs = 0
    sum_inputs = 0
    string_inputs = []
    all_numbers = []

    while True:
        user_input = input("Please enter a number (whole, negative, or decimal.) Press enter to end program: ")
        if user_input == "":
            print("The total number of inputs is: " + str(float(total_inputs)))
            print("The sum of the inputs is: " + str(sum_inputs))
            print("The average of the inputs is: " + str(sum_inputs / total_inputs))
            print("".join(string_inputs))
            break

        try:
            float(user_input)
        except:
            if user_input.isnumeric():
                total_inputs += 1
                sum_inputs += float(user_input)
                continue
            elif user_input.isalpha():
                string_inputs.append(user_input)
                continue
            else:
                print("You cannot mix numbers and letters. Please start over.")
                break
        else:
            total_inputs += 1
            sum_inputs += float(user_input)
            all_numbers.append(float(user_input))
            print(statistics.mean(all_numbers))
            print(statistics.median(all_numbers))
            print(statistics.mode(all_numbers))
            print(statistics.stdev(all_numbers))
            continue


user_statistics()
