##base 60 math language
number = "101"

translated = 0
for i in range(0, len(number)):
    digit = number[i]
    place = 60 ** (len(number)-i-1)
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


"""1 aš, diš, (dili) 
2 min, mìn 
3 eš5
4 limmu, límmu 
5 ía 
6 àš
7 inim, umun5
8 ussu
9 ilimmu
10 u
60 ĝéš(d) (wr. DIŠ)

600 ĝeš(d)u (wr. U+DIŠ)
36000 šár’u (wr. ŠÁRx(UxKASKAL))
3600 šár
"""