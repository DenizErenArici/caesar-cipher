from alphabets import alphabet,alphabet_upper
def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for character in original_text:
        if character.isalpha():
            for i in range(len(alphabet)):
                if character == alphabet[i]:
                    character = alphabet[(i + shift_amount) % len(alphabet)]
                    encrypted_text += character
                    break
                elif character == alphabet_upper[i]:
                    character = alphabet_upper[(i + shift_amount) % len(alphabet_upper)]
                    encrypted_text += character
                    break
        else:
            encrypted_text += character

    print(f"Here is the encoded result: {encrypted_text}")
