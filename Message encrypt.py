# Message Encrypter using Caesar Cipher
def encrypt_message(message, shift):
    encrypted_text = ""
    
    for char in message:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # Non-alphabetic characters remain unchanged
        else:
            encrypted_text += char

    return encrypted_text


def decrypt_message(encrypted_text, shift):
    decrypted_text = ""
    
    for char in encrypted_text:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        # Non-alphabetic characters remain unchanged
        else:
            decrypted_text += char

    return decrypted_text


def main():
    print("=== Message Encrypter ===")
    message = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift key (1-25): "))

    # Encrypt the message
    encrypted_message = encrypt_message(message, shift)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, shift)
    print(f"Decrypted Message: {decrypted_message}")


if __name__ == "__main__":
    main()
