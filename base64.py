from string import uppercase, lowercase, digits

base64Index = uppercase + lowercase + digits + "+/"

def chunk(string):
    """convert one chunk of 3 characters into base 64"""
    padLength = 3 - len(string)
    string += chr(0) * padLength
    

def base64(string):
    result = ""
    while string:
        three_chars = string[:3]
        string = string[3:]
        result += chunk(three_chars)
    return result
