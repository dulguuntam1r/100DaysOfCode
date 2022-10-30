#Eighth day challenge
#Caesar cipher - game of encoding and decoding message

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
game_end = False

def caesar(get_direction, plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            if get_direction == "encode":
                shifted = alphabet.index(letter) + shift_amount
                while shifted > 26:
                    shifted -= 26
            elif get_direction == "decode":
                shifted = alphabet.index(letter) - shift_amount
                while shifted < -26:
                    shifted += 26
            cipher_text += alphabet[shifted]
        else:
            cipher_text += letter
    print(f"The {get_direction}d text is {cipher_text}")

while not game_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if (direction == "encode") or (direction == "decode"):
        caesar(direction, text, shift)
        keep_going = input("Would you like to encode/decode again? Yes or No:\n").lower()
        if keep_going == "no":
            print("Thanks for playing")
            game_end = True
    else:
        print("Wrong input\nThanks for playing")
        game_end = True
