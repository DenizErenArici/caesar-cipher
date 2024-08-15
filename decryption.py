from alphabets import alphabet,alphabet_upper
def decryption(encoded_text, shift_amount):
    decrypted_text = ""
    for character in encoded_text:
        if character.isalpha():
            for i in range(len(alphabet)):
                if character == alphabet[i]:
                    character = alphabet[(i - shift_amount) % len(alphabet)]
                    decrypted_text += character
                    break
                elif character == alphabet_upper[i]:
                    character = alphabet[(i - shift_amount) % len(alphabet_upper)]
                    decrypted_text += character
                    break

        else:
            decrypted_text += character

    print(f"Here is the decrypted result: {decrypted_text}")