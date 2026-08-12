


from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generate the private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Get the public key from the private key
public_key = private_key.public_key()

print("Private key generated!")
print("Public key generated!")

#Encrypt message

message = b"Computer Security Laboratory"
encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Original message:")
print(message.decode())

print("\nEncrypted message:")
print(encrypted_message)

#Decryption message

decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)print("\nDecrypted message:")
print(decrypted_message.decode())

#Trying decryption using public.key
try:
    wrong_decryption = public_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print(wrong_decryption.decode())

except Exception:
    print("\nDecryption using the public key failed.")
