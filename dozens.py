
##dozenal math language
number = "XX01"

translated = 0
for i in range(0, len(number)):
    digit = number[i]
    place = 12 ** (len(number)-i-1)
    print("digit: \t", digit)

    if digit.upper() == "X":
        digit = 10
    elif digit.upper() == "E":
        digit = 11

    #elif digit.upper() == "A":
    #    digit = 12


    register = int(digit)*place
    print(digit, place,  register)
    translated += register

print(translated)
