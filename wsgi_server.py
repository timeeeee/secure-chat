#!! /usr/bin/env python

from wsgiref.simple_server import make_server

# This is our application object. It could have any name,
# except when using mod_wsgi where it must be "application"
def application(environ, start_response):
    # build the response body possibly using the environ dictionary
    response_body = '<br>'.join("%s: %s" % (key, value)
                             for key, value in sorted(environ.items()))
#    response_body = "<html><body><h1>Hi!</h1><p>Some text</p></body></html>"
    status = '200 OK'
 
    # [(Header name, Header value)].
    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
 
    start_response(status, response_headers)
 
    # Return the response body.
    # Notice it is wrapped in a list although it could be any iterable.
    return [response_body]

httpd = make_server('0.0.0.0', 53421, application)

print "starting server"
# httpd.serve_forever() # REALLY forever?!? could not kill with ctrl c
httpd.handle_request()
