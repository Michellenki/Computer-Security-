Diffie–Hellman allows two parties to establish a shared secret over an insecure channel without directly transmitting the secret itself.

The security relies on the difficulty of deriving the private information/shared secret from the public values when properly sized parameters are used.

Alice                         Bob
  |                             |
Private a                    Private b
  |                             |
  ↓                             ↓
Public A  ───────→     ←──── Public B
  |                             |
  ↓                             ↓
B^a mod p                   A^b mod p
  |                             |
  └────────── SAME KEY ─────────┘p
It helps solve the key distribution problem.

Applications:
TLS
VPNs
SSH 