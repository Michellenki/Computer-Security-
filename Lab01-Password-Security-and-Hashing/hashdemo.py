import hashlib

password = input("Enter Password: ")

algorithms = {
    "MD5": hashlib.md5,
    "SHA1": hashlib.sha1,
    "SHA256": hashlib.sha256
}

for name, algorithm in algorithms.items():
    hashed = algorithm(password.encode()).hexdigest()
    print(f"\n{name}")
    print(hashed)