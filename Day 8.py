alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(plain_text, shift_amount, chosen_direction):
  if shift_amount > 25:
    shift_amount = shift_amount % 25
  
  if chosen_direction == "encode":
    cipher_text = ""
    for char in plain_text:
      if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        if new_position > 25:
          new_position = new_position - 26
          new_letter = alphabet[new_position]
        else:
            new_letter = alphabet[new_position]
        cipher_text += new_letter
      else: 
        cipher_text += char
    print(f"The encoded text is {cipher_text}")
  elif chosen_direction == "decode":
    cipher_text = ""
    for char in plain_text:
      if char in alphabet:
        position = alphabet.index(char)
        new_position = position - shift_amount
        if new_position < 0:
          new_position = 26 + new_position
          new_letter = alphabet[new_position]
          cipher_text += new_letter
        else:
          new_letter = alphabet[new_position]
          cipher_text += new_letter
      else: 
        cipher_text += char
    print(f"The decoded text is {cipher_text}")
      



should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  ceaser(text, shift, direction)
  choice = input("Type 'yes' if you want to go again. Otherwise, type 'no.'")
  if choice == 'no':
    should_continue = False
    print("Goodbye!")

