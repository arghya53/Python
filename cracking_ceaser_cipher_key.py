# Here we are going to crack ceaser cipher key with brute_force search
# As the number of keys is small so we can use the brute_force attack to find the key
# here, brute_force means considering all the keys(26) in key space

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def crack_ceaser(cipher_text):
    
    for key in range(len(ALPHABET)):

        plain_text = ''
        

        for c in cipher_text:
            index = ALPHABET.find(c) #numerical representation of the letter
            index= (index-key) % len(ALPHABET) #ceaser_cipher_decryption_eqtn
            plain_text = plain_text + ALPHABET[index] #output
        print('With key %s, the result is %s'%(key, plain_text))

#calling the function inside the same module
if __name__ == '__main__':
    encrypted = 'TBIZLJBWQLWJVWELRPB'
    crack_ceaser(encrypted)
   


