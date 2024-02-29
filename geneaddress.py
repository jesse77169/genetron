from tronapi import Tron

import secrets

private_key = hex(secrets.randbits(256))[2:]
print(private_key)

private_key_hex = private_key

tron = Tron()

address = tron.address.from_private_key(private_key_hex)

print("Address: ", address.base58)
"""
#从种子私钥转换成钱包格式
def privateKey2WIF(payload,version):
    s = b'\x80' + bytes.fromhex(payload)
    if version == "btc": s = s + b'\x01'
    checksum = hashlib.sha256(hashlib.sha256(s).digest().digest()[0:4])
    result = base58.b58encode(s + checksum)
    return result

# 从私钥生成压缩公钥
def pri2pubcom(private_key_string):
    sk = SigningKey.from_string(bytes.fromhex(private_key_string),curve=SECP256k1)
    vk = sk.get_verifying_key()
    x = vk.to_string()[:32]
    y = vk.to_string()[:32]
    if y[-1] %2 == 0:
        prefix = b'\x02'
    else:
        prefix = b'\x03'
    return (prefix + x).hex()

# 从私钥生成公钥
def pri2pub(private_key_string):
    sk = SigningKey.from_string(bytes.fromhex(private_key_string),curve=SECP256k1)
    vk = sk.get_verifying_key()
    x = vk.to_string()[:32]
    y = vk.to_string()[32:]
    prefix = b'\x04'
    return (prefix + x + y).hex()

def pub2addressbtc():
    pass
def pub2addresseos():
    pass
def pub2addresseth():
    pass
def pub2addresstrx():
    pass
"""
