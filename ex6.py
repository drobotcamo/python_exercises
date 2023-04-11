inputPhrase = input("Please enter a string, and I will check if it is a palindrome: \n")

halfLength = len(inputPhrase) // 2
print(inputPhrase[:halfLength])
print(inputPhrase[:len(inputPhrase) - halfLength - 1:-1])

if inputPhrase[:halfLength] == inputPhrase[:len(inputPhrase) - halfLength - 1:-1]:
    print(True)
else:
    print(False)

#pictured above is the hard way to do this
#the only necessary line is really:

print(inputPhrase == inputPhrase[::-1])