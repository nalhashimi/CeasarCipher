import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def perform(operation, original_text, shift_amount):
    if operation == "decode":
        shift_amount *= -1

    output_text = ""
    for letter in original_text:
        if alphabet.count(letter) == 0:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {operation}d result: {output_text}")

rerun = True

while rerun:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    perform(operation=direction, original_text=text, shift_amount=shift)
    rerun = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower() == 'yes'


