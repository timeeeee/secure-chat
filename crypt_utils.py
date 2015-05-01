from Crypto.PublicKey import RSA as CryptoRSA
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random.random import randint

RSA_KEYSIZE = 2048
PUBLIC_EXPONENT = 65537L


def sha(string):
    hash_object = SHA256.new(string)
    return hash_object.digest()


def pad(string, block_size=16):
    # The first 2 bytes of the string will indicate the length of the string
    # Then append random bytes until the length is a multiple of the block size
    length = len(string)
    if length > 2**16 - 1:
        raise ValueError("The maximum string size before padding is 65535.")
    binary_length = chr(length / 256) + chr(length % 256)
    pad_length = block_size - (length + 1) % block_size - 1
    pad = "".join(chr(randint(0, 255)) for _ in range(pad_length))
    return binary_length + string + pad


def unpad(string):
    tens, ones = string[:2]
    length = ord(tens) * 256 + ord(ones)
    return string[2:2 + length]


class RSA:
    def __init__(self, n=None, d=None):
        self.e = PUBLIC_EXPONENT
        self.n = n
        self.d = d

        if n is None:
            self.key_object = CryptoRSA.generate(2048)
            self.n = self.key_object.n
            self.d = self.key_object.d
        elif d is None:
            self.key_object = CryptoRSA.construct((self.n, self.e))
        else:
            self.key_object = CryptoRSA.construct((self.n, self.e, self.d))

    def encrypt(self, msg):
        return self.key_object.encrypt(msg, 0)

    def decrypt(self, msg):
        if self.d is None:
            raise NotImplementedError(
                "This RSA object does not contain a private key.")
        return self.key_object.decrypt(msg)

    def getPublicKey(self):
        return self.n

    def getPrivateKey(self):
        if self.d is None:
            raise NotImplementedError(
                "This RSA object does not contain a private key.")
        return self.d


def aes_encrypt(msg, key):
    padded_msg = pad(msg)
    aes_object = AES.new(sha(key))
    return aes_object.encrypt(pad(msg))


def aes_decrypt(msg, key):
    aes_object = AES.new(sha(key))
    return unpad(aes_object.decrypt(msg))
