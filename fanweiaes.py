from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib
import binascii

class SHA1PRNG:
    def __init__(self, seed):
        self.seed = seed
        self.digest = hashlib.sha1(seed).digest()

    def next_bytes(self, num_bytes):
        result = bytearray()
        while len(result) < num_bytes:
            self.digest = hashlib.sha1(self.digest).digest()
            result.extend(self.digest)
        return bytes(result[:num_bytes])

def init_secret_key(key):
    prng = SHA1PRNG(key.encode())
    return prng.next_bytes(16)

def encrypt(data, key):
    cipher = AES.new(init_secret_key(key), AES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    return binascii.hexlify(encrypted_bytes).decode().lower()

def startvuln(id):
    receiver = str(id)
    timestamp = "1"
    syscode = "1"
    secretkey = "u6skkR"
    encodeAuth = encrypt(receiver + timestamp, syscode + secretkey)
    return encodeAuth


