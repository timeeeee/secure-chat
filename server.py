#! /usr/bin/env python

from wsgiref.simple_server import make_server
import sqlite3
import json

database = sqlite3.connect("chat.db")

# This is our application object. It could have any name,
# except when using mod_wsgi where it must be "application"
def application(environ, start_response):
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
        response_body = json.dumps({"online": ["Jimbo"], "new_messages": ["this is a TOTALLY ENCRYPTED message"]})
        status = "200 OK"
        response_headers = [('Content-Type', 'application/json'),
                            ('Content-Length', str(len(response_body)))]

    elif environ["PATH_INFO"] == "/oldmessages":
        old_messages = ["encrypted message 1", "encrypted message 2", "encrypted message 3"]
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
        response_body = json.dumps({"success": True})
        status = "200 OK"
        response_headers = [('Content-Type', 'application/json'),
                            ('Content-Length', str(len(response_body)))]
        

    start_response(status, response_headers)
    return [response_body]

httpd = make_server('0.0.0.0', 53421, application)

print "starting server"
# httpd.serve_forever() # REALLY forever?!? could not kill with ctrl c
httpd.handle_request()
