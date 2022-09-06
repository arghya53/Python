# Here I have used ceaser_cipher algorithm to encrypt and decrypt a message
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3

def ceaser_encrypt(plain_text, KEY):
    # the encrypted message
    cipher_text = ''
    # we make the algorithm case insensitive
    plain_text = plain_text.upper()

    # consider all the letters are in plain_text
    for c in plain_text:
        # when we put a value of "c", we get the numerical representation (index) with that character in ALPHABET 
        index = ALPHABET.find(c) # finding index of the given letter
        # ceaser encryption is the simple shift or increment of characters according to the key and we need to use
        # modular arithmetic within the range [0, number_of_letters_in_the_alphabet]
        
        index = (index + KEY) % len(ALPHABET) # applying ceaser_cipher formula
        
        # keep appending the given letter to the cipher text

        cipher_text = cipher_text + ALPHABET[index]

    return cipher_text


def ceaser_decrypt(cipher_text, KEY):


    plain_text= ''

    cipher_text = cipher_text.upper()

    for c in cipher_text:

        index = ALPHABET.find(c) #numerical conversion(index) of any letter c


        index = (index-KEY) % len(ALPHABET) # transformation of the index
            
            # now we find the alphabet associated with the newly found index and append it to plain_text
        plain_text = plain_text + ALPHABET[index] 
             
    return plain_text  

# now testing the function

if __name__ == '__main__': # it is because the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”
    m = "Welcome to my house"
    encrypted = ceaser_encrypt(m, 3)
    print (encrypted)
    print(ceaser_decrypt(m, 3))








