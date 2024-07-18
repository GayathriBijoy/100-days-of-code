#caesar-cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


  
  
def encrypt(text , shift):
    cipher_text=[]
    
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            cipher_text.append(alphabet[ ((index + 1)%len(alphabet)) + shift-1])
        
    print(f'the encoded text is {"".join(cipher_text)}')    

def decode(text, shift):
    decipher_text=[]
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            decipher_text.append(alphabet[ ((index + 1)%len(alphabet)) - shift-1])

    print(f'the encoded text is {"".join(decipher_text)}')   




      
if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decode(text,shift)
else:
    print("invalid input for text, try again")


