def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result

text = input("Enter the text to be encrypted: ")
shift = int(input("Enter the shift value: "))

encrypted_text = caesar_cipher(text, shift)
print("Encrypted Text:", encrypted_text)
