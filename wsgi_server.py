#!! /usr/bin/env python

from wsiref.simple_server import make_server

# This is our application object. It could have any name,
# except when using mod_wsgi where it must be "application"
def application(environ, start_response):
    # build the response body possibly using the environ dictionary
    reponse_body = '\n'.join("%s: %s" % (key, value)
                             for key, value in sorted(environ.items()))
    status = '200 OK'
 
    # [(Header name, Header value)].
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
 
    start_response(status, response_headers)
 
    # Return the response body.
    # Notice it is wrapped in a list although it could be any iterable.
    return [response_body]

httpd = make_server('localhost', 53421, application)

httpd.handle_request()
