from cryptography.fernet import Fernet

# Generate a secret key
key = Fernet.generate_key()

# Create the encryption tool
cipher = Fernet(key)

# Our original message
message = b"Computer Security Laboratory"

# Encrypt the message
encrypted_message = cipher.encrypt(message)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)

print("Original message:")
print(message.decode())

print("\nSecret key:")
print(key.decode())

print("\nEncrypted message:")
print(encrypted_message.decode())

print("\nDecrypted message:")
print(decrypted_message.decode())
