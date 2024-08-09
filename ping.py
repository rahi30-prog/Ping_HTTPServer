from http.server import BaseHTTPRequestHandler, HTTPServer  # BaseHTTPRequestHandler is used to handle HTTP requests.

# CustomHTTPRequestHandler: Handles the HTTP requests sent to the server.
class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':
            # Send 200 OK response
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Found it!!')
        else:
            # Send 404 Not Found response
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8000):
    global httpd
    # server_class=HTTPServer: By default, the server class is set to HTTPServer.
    # handler_class=CustomHTTPRequestHandler: By default, the request handler class is set to CustomHTTPRequestHandler.
    # port=8000: By default, the server will listen on port 8000.
    server_address = ('', port)  # A tuple containing the address the server will listen on. (port is set to 8000)
    httpd = server_class(server_address, handler_class)  # Creates an instance of the server using the specified address and request handler class.
    print(f'Server running on port {port}')
    httpd.serve_forever()  # Starts the server and keeps it running indefinitely

if __name__ == '__main__':
    run()
