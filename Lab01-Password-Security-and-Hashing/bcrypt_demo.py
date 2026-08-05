"""
Production-Grade Password Hashing 

hashlib + a manual salt (see salting_demo.py) is useful for teaching
the concept, but real systems should use a purpose-built password
hashing algorithm such as bcrypt, scrypt, or Argon2. These are
deliberately slow and handle the salt automatically, which makes
brute-force attacks far more expensive for an attacker.


"""

try:
    import bcrypt
except ImportError:  # pragma: no cover
    raise SystemExit(
        "bcrypt is not installed.\n"
        "Install it with: pip install bcrypt --break-system-packages"
    )


def hash_password(password: str) -> bytes:
    # rounds = cost factor. Higher = slower to compute = more resistant
    # to brute force, at the cost of server CPU time.
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode(), salt)


def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)


if __name__ == "__main__":
    pw = "CyberSecurity2026"
    hashed = hash_password(pw)

    print(f"Password    : {pw}")
    print(f"bcrypt hash : {hashed.decode()}")

    print("\nVerifying correct password :", verify_password(pw, hashed))
    print("Verifying wrong password   :", verify_password("wrongpass", hashed))