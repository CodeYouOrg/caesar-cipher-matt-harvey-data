alphabet = 'abcdefghijklmnopqrstuvwxyz'

shift = input("Please enter the number of places to shift value: ")

coded = 'zebras are neat!'

sentence = ''

for letter in coded.lower():
    n = int(shift) % 26
    if letter in alphabet:
        m = alphabet.index(letter)
        sentence += alphabet[(m + n) % 26]
    else:
        sentence += letter

print(sentence)# add your code here
