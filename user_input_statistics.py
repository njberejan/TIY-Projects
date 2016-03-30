def user_statistics():

    total_inputs = 0
    sum_inputs = 0
    string_inputs = []

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
            try:
                # print("a string")
                # print(user_input.isnumeric())
                # print(user_input.isalpha())
                if user_input.isnumeric():

                elif user_input.isalpha():
                else:
            except:
                print("You cannot mix numbers and letters. Please start over.")
                break
            else:
                string_inputs.append(user_input)
                continue
        else:
            total_inputs += 1
            sum_inputs += float(user_input)
            continue


user_statistics()
