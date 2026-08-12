# Public parameters
p = 23
g = 5

# Alice's private number
a = 6

# Bob's private number
b = 15

# Alice calculates her public value
A = pow(g, a, p)

# Bob calculates his public value
B = pow(g, b, p)

# Alice calculates the shared secret
alice_secret = pow(B, a, p)

# Bob calculates the shared secret
bob_secret = pow(A, b, p)

print("Public parameters:")
print("p =", p)
print("g =", g)

print("\nAlice's public value:")
print(A)

print("\nBob's public value:")
print(B)

print("\nAlice's shared secret:")
print(alice_secret)

print("\nBob's shared secret:")
print(bob_secret)

print("\nDo both secrets match?")
print(alice_secret == bob_secret)
