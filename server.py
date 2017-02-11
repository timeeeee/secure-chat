from datetime import datetime
import json
import hmac
from time import time as epoch
from hashlib import sha256

from flask import Flask, Response, request, jsonify
app = Flask(__name__)


TOKEN_SECRET = ("\xc1\xf1\"\xe2J\x93\x10y+\xef\xdd\x9dJF\x04\x8e='\xe3\x9b."
                "\xf0\xab\xeeI\xfd\xd6\xf0:D5\x04K:\xa2\xd9\xaf\xb6\xfc\x1c"
                "\xf4^{\x98\x80\xed{\xdb\xf1W\x01\xca\x98Pt\x97\n\xfd\xa0\xe5("
                "kZ\xdd\xbfif7\x9b\xd4A\xfad\x19c'\x1f\x98\xdb\x18&>\x01\x01"
                "\xacF\x1dn\xf8{SK\xb0C\xa2\x7f\xb5\xef\x146R\xa8S\xd1\x1f5"
                "\xe8s\xde\xc3A\xc2\xc2\x897\xb3\x194@\x05\x887?\xfb\x90r!\x13"
                )
MAX_TOKEN_AGE = 60 * 10


def make_token(name, secret):
    """Generate a token for right now with the given username and secret."""
    timestamp = str(int(epoch()))
    hmac_obj = hmac.new(secret, name + timestamp, sha256)
    return ",".join((name, timestamp, hmac_obj.hexdigest()))


def verify_token(token, secret):
    name, timestamp, token_hash = token.split(",")
    if epoch() - timestamp > MAX_TOKEN_AGE:
        return False
    hmac_obj = hmac.new(secret, name, timestamp)
    correct_token = ",".join([name, timestamp, hmac_obj.hexdigest()])
    return hmac.compare_digest(token, correct_token)


token = make_token("timbo", TOKEN_SECRET)
print token
assert verify_token(make_token(token, TOKEN_SECRET), TOKEN_SECRET)


def require_login():
    """
    A decorator that checks the request header for user id, epoch time of the
    last request, and matching token. If any elements are missing or the token
    doesn't match, send back a 405 error. If the user is authenticated, set a
    new timestamp and token to verify it.
    """
    pass


@app.route("/")
def api_root():
    return "Welcome."


@app.route("/users/<user_id>", methods=["GET"])
def users(user_id):
    return "user {}".format(user_id)


@app.route("/messages/<message_id>", methods=["GET"])
def messages(message_id):
    return "reading message {}".format(message_id)


@app.route("/messages", methods=["POST"])
def post_messages():
    if request.headers["Content-Type"] == "application/json":
        # If we got a request with json, serve the same data back with a timestamp
        data = request.json.copy()
        data['timestamp'] = datetime.utcnow().isoformat()
        response = jsonify(data)
        response.status_code = 200
        return response
    else:
        return Response("415 Unsupported Media Type", status=415)


if __name__ == "__main__":
    app.run()
