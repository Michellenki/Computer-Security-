import hashlib


def hash_password(password: str, algorithm: str) -> str:
    """Return the hex digest of `password` using the given hash algorithm."""
    h = hashlib.new(algorithm)
    h.update(password.encode("utf-8"))
    return h.hexdigest()


def demo_algorithms(password: str) -> None:
    print(f"\nPassword: {password!r}")
    print("-" * 60)
    print(f"{'Algorithm':<10}{'Output length':<16}Hash")
    print("-" * 60)
    for algo in ("md5", "sha1", "sha256"):
        digest = hash_password(password, algo)
        print(f"{algo.upper():<10}{len(digest):<16}{digest}")


def demo_avalanche_effect(password: str) -> None:
    print("\nAvalanche Effect Demonstration (SHA-256)")
    print("-" * 60)
    original = hash_password(password, "sha256")
    print(f"Original password : {password!r}")
    print(f"Original SHA-256  : {original}")

    # Flip a single character in the password
    last_char = password[-1]
    new_char = "1" if last_char != "1" else "2"
    modified = password[:-1] + new_char
    changed = hash_password(modified, "sha256")

    print(f"\nModified password : {modified!r}  (last character changed)")
    print(f"Modified SHA-256  : {changed}")

    diff = sum(a != b for a, b in zip(original, changed))
    print(f"\nHex characters that differ: {diff} / {len(original)}")
    print("Conclusion: A single character change produces a completely")
    print("different hash. This property is called the AVALANCHE EFFECT,")
    print("and it is one reason cryptographic hashes are useful for")
    print("detecting even the smallest change to data or a password.")


if __name__ == "__main__":
    test_password = "CyberSecurity2026"
    demo_algorithms(test_password)
    demo_avalanche_effect(test_password)