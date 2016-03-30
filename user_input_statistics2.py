total_inputs = 0
sum_inputs = 0
average_inputs = 0

while True:
    user_input = input("Please enter a number (whole, negative, or decimal.) Press enter to end program: ")
    if user_input == "":
        print("The total number of inputs is: " + str(float(total_inputs)))
        print("The sum of the inputs is: " + str(sum_inputs))
        print("The average of the inputs is: " + str(sum_inputs / total_inputs))
        break

    try:
        float(user_input)
    except:
        print("That is not a number! Please try again.")
        continue
    else:
        total_inputs += 1
        sum_inputs += float(user_input)
        continue
