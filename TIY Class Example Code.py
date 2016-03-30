#code examples day 1:

#while loop example:
counter = 0
while True:
    counter += 1
    if counter >= 10:
        break
    if counter % 2 == 1:
        continue
    print(counter)

#error handling example:
def is_float(value):
    try:
        float(value)
    except:
        return False
    return True
