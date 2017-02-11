from Crypto.PublicKey import RSA as CryptoRSA
from Crypto.Hash import SHA512
from Crypto.Cipher import AES
from Crypto.Random.random import randint


def sha(string):
    """
    Calculate the 512 bit SHA hash of a string.
    """
    hash_object = SHA512.new(string)
    return hash_object.digest()


def rsa_encrypt(msg, public_key):
    """
    Encrypt a message with RSA using the recipient's public key.
    """
    pass


def rsa_decrypt(msg, private_key):
    """
    Decrypt a message with RSA using the recipient's private key.
    """
    pass


def aes_encrypt(msg, key):
    """
    Encrypt a message with AES using a 256 bit key.
    """
    padded_msg = pad(msg)
    aes_object = AES.new(sha(key))
    return aes_object.encrypt(pad(msg))


def aes_decrypt(msg, key):
    """
    Decrypt a message with AES using a 256 bit key.
    """
    aes_object = AES.new(sha(key))
    return unpad(aes_object.decrypt(msg))
