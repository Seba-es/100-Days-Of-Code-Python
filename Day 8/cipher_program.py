# Caesar Cipher
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

program = True


def caesar(start_text, shift_amount, cipher_direction):
    word_code = ""
    for letter in start_text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            if cipher_direction == "encode":
                if letter_index + shift_amount > 25:
                    letter_index = letter_index - 25 - 1  # -1 por el index 0
                word_code += alphabet[letter_index + shift_amount]
            elif cipher_direction == "decode":
                if letter_index - shift_amount < 0:
                    letter_index = letter_index + 25 + 1  # 1 por el index 0
                word_code += alphabet[letter_index - shift_amount]
        else:
            word_code += letter

    print(f"The {cipher_direction} text is {word_code}")


while program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    reset = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")

    if reset == "no":
        program = False
        print("Goodbye")

while shift >= 38:
    print("The shift number must be between 1 and 37")
    shift = int(input("Type the shift number:\n"))
