# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:



def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  
            shifted = ord(char) + shift
            
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
            
    return encrypted_text

input_text = input("Geef de tekst die wilt encrypten:\n")

result = encrypt(input_text, 5)

print(result)