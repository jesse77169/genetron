from tronapi import Tron

import secrets

private_key = hex(secrets.randbits(256))[2:]
print(private_key)

private_key_hex = private_key

tron = Tron()

address = tron.address.from_private_key(private_key_hex)

print("Address: ", address.base58)

