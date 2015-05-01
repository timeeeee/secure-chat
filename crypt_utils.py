from Crypto.PublicKey import RSA as CryptoRSA
from Crypto.Hash import SHA256
from Crypto.Cipher import AES

RSA_KEYSIZE = 2048
PUBLIC_EXPONENT = 65537L


def sha(string):
    hash_object = SHA256.new(string)
    return hash_object.digest()


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
            raise NotImplementedError("This RSA object does not contain a private key.")
        return self.key_object.decrypt(msg)
    def getPublicKey(self):
        return self.n

    def getPrivateKey(self):
        if self.d is None:
            raise NotImplementedError("This RSA object does not contain a private key.")
        return self.d
    
            
