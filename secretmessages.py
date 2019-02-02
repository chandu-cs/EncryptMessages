alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = input('Please enter a key: ')
enteredKey = int(key)
newMessage = ''
message = input('Please enter a message: ')
for character in message:
     if character in alphabet: #checking if character is in alphabet
         position = alphabet.find(character)
#Encryption
         newPosition = (position + enteredKey) % 26
         newCharacter = alphabet[newPosition]
#Adding characters to new message variable
         newMessage += newCharacter
else:
    newMessage += character
print(newMessage)

