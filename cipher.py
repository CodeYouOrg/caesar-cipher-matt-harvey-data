alphabet = 'abcdefghijklmnopqrstuvwxyz'

shift = input("Please enter the number of places to shift value: ")

coded = input("Please type the sentence you would like to encrypt: ")

sentence = ''

for letter in coded.lower():
    n = int(shift) % 26
    if letter in alphabet:
        m = alphabet.index(letter)
        sentence += alphabet[(m + n) % 26]
    else:
        sentence += letter

print(sentence)# add your code here
