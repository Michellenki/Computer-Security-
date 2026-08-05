

Demonstrates password salting: why identical passwords must NOT
produce identical stored hashes, and how a random per-user salt
solves this problem.




import hashlib
import os


def hash_without_salt(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def generate_salt(length: int = 16) -> bytes:
    """Generate a cryptographically secure random salt."""
    return os.urandom(length)


def hash_with_salt(password: str, salt: bytes) -> str:
    return hashlib.sha256(salt + password.encode()).hexdigest()


def demo_unsalted_collision() -> None:
    print("Scenario 1: Two users choose the SAME password (no salt)")
    print("-" * 60)
    password = "Password123"
    user_a_hash = hash_without_salt(password)
    user_b_hash = hash_without_salt(password)
    print(f"User A password: {password!r} -> {user_a_hash}")
    print(f"User B password: {password!r} -> {user_b_hash}")
    print(f"Identical stored hashes? {user_a_hash == user_b_hash}")
    print("\nProblem: If an attacker cracks or looks up one hash (e.g. via")
    print("a precomputed rainbow table), they instantly know every other")
    print("account in the database using that same password.")


def demo_salted_solution() -> None:
    print("\nScenario 2: Same password, but each user has a unique salt")
    print("-" * 60)
    password = "Password123"

    salt_a = generate_salt()
    salt_b = generate_salt()

    hash_a = hash_with_salt(password, salt_a)
    hash_b = hash_with_salt(password, salt_b)

    print(f"User A salt: {salt_a.hex()}")
    print(f"User A hash: {hash_a}")
    print(f"\nUser B salt: {salt_b.hex()}")
    print(f"User B hash: {hash_b}")
    print(f"\nIdentical stored hashes? {hash_a == hash_b}")
    print("\nEach user's stored record is the pair (salt, hash). Even with")
    print("an identical password, the resulting hashes differ, which")
    print("defeats precomputed rainbow-table attacks and prevents an")
    print("attacker from spotting duplicate passwords across accounts.")


if __name__ == "__main__":
    demo_unsalted_collision()
    demo_salted_solution()