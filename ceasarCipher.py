def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + key) % 26 + offset)
        else:
            result += char
    return result

def decrypt(text, key):
    return encrypt(text, -key)

def auto_decrypt(text):
    print("\n🔍 Trying all possible Caesar Cipher shifts:\n")
    for key in range(1, 26):
        decrypted = ""
        for char in text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                decrypted += chr((ord(char) - offset - key) % 26 + offset)
            else:
                decrypted += char
        print(f"Key {key:2}: {decrypted}")

def main():
    print("🔐 Caesar Cipher (Encrypt / Decrypt / Auto-Decrypt)")
    choice = input("1: Encrypt\n2: Decrypt\n3: Auto-Decrypt\nSelect: ")

    if choice == "1":
        text = input("Enter your text: ")
        key = int(input("Enter key (number): "))
        encrypted = encrypt(text, key)
        print("🔒 Encrypted text:", encrypted)

    elif choice == "2":
        text = input("Enter your encrypted text: ")
        key = int(input("Enter key (number): "))
        decrypted = decrypt(text, key)
        print("🔓 Decrypted text:", decrypted)

    elif choice == "3":
        text = input("Enter encrypted text for auto-decryption: ")
        auto_decrypt(text)

    else:
        print("❌ Invalid selection!")

if __name__ == "__main__":
    main()