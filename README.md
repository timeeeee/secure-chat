Encrypted Chat
==============

The purpose of this project is to have both a server and client that together
provide an end-to-end encrypted chat.


Server
------

The server, implemented in Python using Flask, provides an API that provides
the following:

- GET /users - get a list of users.
- GET /users/<id> - get a user's public key, and if the user is authenticated,
  their encrypted private key and the salt used in decrypting it.
- GET /messages - get a timestamp and ID for messages to the authenticated
  user. This needs url parameters to filter by time range, sender, and maybe a
  maximum number of results.
- POST /messages - send a message, given a recipient, encrypted message, its
  session key, and a signature.
- GET /messages/<id> - get a particular message, including sender, session key,
  signature, encrypted message, and timestamp.

The user will authenticate themselves with the server by sending a hash of
their password, which the server will check by adding a salt, hashing it again,
and comparing with the expected result. After the user is authenticated, the
server will send a token with each response (username, timestamp, and keyed
hash of these) so that the user can use this in future requests.

Since the server doesn't have to do any of the actual encryption, it can be
tested with plaintext messages.


Client
------

First we will implement a terminal-based client in Python. Later it would be
nice to implement a client in a web page using ajax to communicate with the
server.

The general workflow for a client should look like this: Request a password
from the user. Hash it and use it to authenticate with the server. Request the
users private key from the server. Use a key-stretching function and use the
result to decrypt the user's private key.

To send a message, the client will generate the following information to send
to the server:

- A randomly generated session key, encrypted with the recipients public key.
- The message, encrypted with the session key.
- A signature (the plaintext hashed and signed with the senders private key)

To receive a message, the client reverses the process: Use their private key to
decrypt the session key, use the session key to decrypt the message, and verify
that the signature matches the hashed plaintext.


Algorithms
----------

Symmetric encryption: AES-256
Asymmetric encryption: RSA, 4096 bit keys
Hash: SHA-512
Key stretching: PBKDF2


crypt_utils
-----------

crypt_utils.py includes a number of functions to make it easy to apply the
encryption and hash algorithms.

