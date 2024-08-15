from alphabets import alphabet,alphabet_upper
ifcontinue="yes"
while(ifcontinue=="yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    def caesar(original_text, shift_amount, encode_or_decode):
        output_text = ""
        if encode_or_decode == "encode":
            shift_amount *= 1
        elif encode_or_decode == "decode":
            shift_amount *= -1
        for character in original_text:
            if character.isalpha():
                for i in range(len(alphabet)):
                    if character == alphabet[i]:
                        character = alphabet[(i + shift_amount) % len(alphabet)]
                        output_text += character
                        break
                    elif character == alphabet_upper[i]:
                        character = alphabet_upper[(i + shift_amount) % len(alphabet_upper)]
                        output_text += character
                        break
            else:
                output_text += character

        print(f"Here is the {encode_or_decode}d result: {output_text}")


    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    ifcontinue = input("Type 'yes' if you want to go again,otherwise type 'no':").lower()

print("Goodbye then.")
