# secure_file_crypto.py

from cryptography.fernet import Fernet
import os

# --- Generate a key and save/load it securely ---
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

# --- Encrypt the file ---
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"[+] File encrypted successfully: {file_path}.enc")

# --- Decrypt the file ---
def decrypt_file(enc_file_path, output_path):
    key = load_key()
    fernet = Fernet(key)

    with open(enc_file_path, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(output_path, "wb") as dec_file:
        dec_file.write(decrypted)

    print(f"[+] File decrypted successfully: {output_path}")

# --- Main menu ---
if __name__ == "__main__":
    if not os.path.exists("secret.key"):
        generate_key()
        print("[*] Encryption key generated and saved as secret.key")

    print("Choose an option:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        file_to_encrypt = input("Enter the file path to encrypt: ")
        encrypt_file(file_to_encrypt)
    elif choice == "2":
        enc_file = input("Enter the path of the encrypted file (.enc): ")
        output_file = input("Enter output file name to save decrypted content: ")
        decrypt_file(enc_file, output_file)
    else:
        print("Invalid choice.")
