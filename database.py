import sqlite3
from string import lowercase, uppercase, digits
from getpass import getpass
from sys import argv
from os.path import isfile
from crypt_utils import sha, aes_encrypt, aes_decrypt, RSA

'''
database.py is a collection of functions to manage the database.
  create: creates an empty database. 
  adduser username: create user with the given name. Will prompt for password.
'''

USERNAME_CHARS = lowercase + uppercase + digits
DEFAULT_DATABASE = "chat.db"
RSA_KEYSIZE = 2048
USAGE = {
    None: ("Usage: python database.py _command_ [parameters]\n"
           "\n"
           "Commands:\n"
           "  adduser _username_ [database]\n"
           "  create [database]\n"
           "\n"
           "The default database is {}").format(DEFAULT_DATABASE),
    'adduser': ("Usage: python database.py adduser _username_ database\n"
                "This will prompt for a password, and add tables for the "
                "new user to the database. The default database is "
                "{}.").format(DEFAULT_DATABASE),
    'create': ("Usage: python database.py create [database]\n"
               "Creates empty database for a chat server. The default"
               "database is {}.").format(DEFAULT_DATABASE),
    }


def isValidUsername(name):
    for char in name:
        if not(char in USERNAME_CHARS):
            return False
    return True

def adduser(name, database=DEFAULT_DATABASE):
    # make sure username is valid
    if not(isValidUsername(name)):
        raise ValueError("Username can only contain uppercase and lowercase"
                         "characters and digits")
    
    # make sure there isn't already a table for this username
    db = sqlite3.connect(database)
    query = "SELECT name FROM sqlite_master WHERE type='table' AND name='?';"
    existing_table = db.execute(query, name).fetchone()
    if existing_table:
        error_msg = "A table with the name '{}' already exists."
        raise ValueError(error_msg.format(name))

    # get new password
    password = getpass()
    password_repeat = getpass("Repeat:")
    if password != password_repeat:
        raise ValueError("Passwords don't match.")

    # make password hashes
    hash_object = SHA256.new(password)
    password_hash = hash_object.digest()
    hash_object = SHA256.new(password_hash)
    password_double_hash = hash_object.digest()
    print "Hash is \"{}\".".format(password_hash)
    print "Double hash is \"{}\".".format(password_double_hash)

    # generate public and private keys
    key_object = RSA()
    private_key = key_object.getPrivateKey()
    public_key = key_object.getPublicKey()

    print "New user '{}' created with password '{}'.".format(name, password)

    
def create(database=DEFAULT_DATABASE):
    if isfile(database):
        raise ValueError("The file {} already exists.".format(database))
    else:
        print "Going to create database file {}".format(database)
        db = sqlite3.connect(database)
        db.execute("CREATE TABLE users(name TEXT, password_double_hash TEXT,"
                   "public_key TEXT, encrypted_private_key TEXT")


def printUsage(command=None):
    if not(command in USAGE):
        command = None
    print USAGE[command]


if __name__ == "__main__":
    if len(argv) == 1:
        printUsage()
    else:
        if argv[1] == "adduser":
            if len(argv) == 3:
                adduser(argv[2])
            elif len(argv) == 4:
                adduser(argv[2], argv[3])
            else:
                printUsage("adduser")
        elif argv[1] == "create":
            if len(argv) == 2:
                create()
            else:
                create(argv[2])
