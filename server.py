#! /usr/bin/env python

from wsgiref.simple_server import make_server
import sqlite3
import json
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

database = sqlite3.connect("chat.db")


class Server:
    def __init__(self, database):
        self.database = sqlite3.connect(database)

    def run(self, host='0.0.0.0', port=53421):
        httpd = make_server(host, port, self.application)
        print "starting server"
        httpd.serve_forever()

    def application(self, environ, start_response):
        if environ["PATH_INFO"] == "/":
            # build the response body possibly using the environ dictionary
            response_body = '<br>'.join("%s: %s" % (key, value)
                                        for key, value in sorted(environ.items()))
            status = "200 OK"
            response_headers = [('Content-Type', 'text/html'),
                                ('Content-Length', str(len(response_body)))]
    
        # Get userlist
        elif environ["PATH_INFO"] == "/userlist":
            response_body = json.dumps(["Bryan", "Jimbo"])
            status = "200 OK"
            response_headers = [('Content-Type', 'application/json'),
                                ('Content-Length', str(len(response_body)))]
    
        # Update - get new messages and online users
        elif environ["PATH_INFO"] == "/update":
            new_messages = ["this is a TOTALLY ENCRYPTED message"]
            user_list = ["Jimbo"]
            response_body = json.dumps({"online": user_list,
                                        "new_messages": new_messages})
            status = "200 OK"
            response_headers = [('Content-Type', 'application/json'),
                                ('Content-Length', str(len(response_body)))]
    
        elif environ["PATH_INFO"] == "/oldmessages":
            old_messages = ["encrypted message 1",
                            "encrypted message 2",
                            "encrypted message 3"]
            response_body = json.dumps(old_messages)
            status = "200 OK"
            response_headers = [('Content-Type', 'application/json'),
                                ('Content-Length', str(len(response_body)))]
    
        elif environ["PATH_INFO"] == "/sendmessage":
            try:
                request_body_size = int(environ["CONTENT_LENGTH"])
            except(ValueError):
                request_body_size = 0
            message = environ["wsgi.input"].read(request_body_size)
            response_body = json.dumps({"success": True, "message": message})
            status = "200 OK"
            response_headers = [('Content-Type', 'application/json'),
                                ('Content-Length', str(len(response_body)))]
    
        start_response(status, response_headers)
        return [response_body]


if __name__ == "__main__":
    server = Server("chat.db")
    server.run()
