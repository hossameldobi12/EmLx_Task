'''
write a python program to test whether a passed letter is a vowel or not
Name : Hossam Adel Mostafa

'''

letter = input("plz entre the letter\n")
lower = (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u')
upper = (letter == 'A') or (letter == 'E') or (letter == 'I') or (letter == 'O') or (letter == 'U')
if lower == 1 :
    print("the letter is lower vewel")
elif upper == 1 :
    print("the letter is upper vowel")
else :
    print("the letter is not vowel")