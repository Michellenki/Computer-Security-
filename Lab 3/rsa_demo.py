


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